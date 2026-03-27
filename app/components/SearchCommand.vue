<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import MiniSearch from "minisearch";
import { Search } from "lucide-vue-next";
import { useActiveElement, useMagicKeys } from "@vueuse/core";
import type { PageCollections } from "@nuxt/content";
import { cn } from "~/lib/utils";

const props = defineProps<{
    collection: keyof PageCollections;
    class?: HTMLAttributes["class"];
}>();

const activeElement = useActiveElement();
const { Meta_K, Ctrl_K, Slash } = useMagicKeys({
    passive: false,
    onEventFired(e) {
        if (
            (e.key === "k" && (e.metaKey || e.ctrlKey)) ||
            (e.key === "/" && notUsingInput.value)
        )
            e.preventDefault()
    },
});

const { data } = await useAsyncData(`${props.collection}-search`, () => queryCollectionSearchSections(props.collection), {
    watch: [() => props.collection]
});

const open = ref(false);
const query = ref("");
const modifierKeySymbol = ref("ctrl");

const result = computed(() => miniSearch.search(toValue(query)));
const notUsingInput = computed(() => activeElement.value?.tagName !== "INPUT" && activeElement.value?.tagName !== "TEXTAREA");

const miniSearch = new MiniSearch({
    fields: ["title", "content"],
    storeFields: ["title", "content"],
    searchOptions: {
        prefix: true,
        fuzzy: 0.2,
    },
});

// Add data to the MiniSearch instance
miniSearch.addAll(toValue(data.value));

function handleOpenChange() {
    open.value = !open.value;
}

watch([Meta_K, Ctrl_K, Slash], (v) => {
    if (v[0] || v[1] || (v[2] && notUsingInput.value)) {
        handleOpenChange();
    }
});

watch(open, (newValue) => {
    if (!newValue) {
        query.value = "";
    }
});

watch([() => props.collection, data], (newValue) => {
    miniSearch.removeAll();
    miniSearch.addAll(toValue(newValue[1]));
});

onMounted(() => {
    if (import.meta.client && navigator.platform.startsWith("Mac")) {
        modifierKeySymbol.value = "⌘";
    }
});
</script>

<template>
    <Button variant="ghost" size="icon" :class="cn('md:w-[160px] font-normal md:text-tertiary-foreground md:border md:px-2', props.class)" @click="open = true">
        <Search />
        <span class="hidden md:flex">Search...</span>
	    <div class="hidden md:inline-flex gap-1">
		    <Kbd>{{ modifierKeySymbol }}</Kbd>
		    <Kbd>K</Kbd>
	    </div>
    </Button>
    <CommandDialog v-model:open="open">
        <CommandInput v-model="query" placeholder="Search..." />
        <CommandList>
            <CommandEmpty>No results found.</CommandEmpty>
            <CommandGroup heading="Suggestions">
                <CommandItem v-for="link of result" :key="link.id" :value="link.id" class="cursor-pointer gap-1 py-2" as-child @select="open = false">
                    <NuxtLink :to="link.id" class="flex flex-col items-start">
                        <div>{{ link.title }}</div>
                        <p class="text-muted-foreground/80 text-xs">{{ link.content }}</p>
                    </NuxtLink>
                </CommandItem>
            </CommandGroup>
        </CommandList>
    </CommandDialog>
</template>