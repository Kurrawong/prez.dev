<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import type { PageCollections } from "@nuxt/content";
import { ChevronDown, ChevronUp, Github, ExternalLink } from "lucide-vue-next";
import { cn } from "~/lib/utils";

const route = useRoute();

const props = defineProps<{
    collection: keyof PageCollections;
    class?: HTMLAttributes["class"];
}>();

const { data } = await useAsyncData(`${props.collection}-navigation`, () => {
    return queryCollectionNavigation(props.collection, ["tags"]);
    // return queryCollectionNavigation(props.collection);
});
</script>

<template>
    <nav :class="cn('flex flex-col grow', props.class)">
        <template v-for="item in data?.[0].children">
            <Collapsible v-if="item.children" v-slot="{ open }" :defaultOpen="route.path.startsWith(item.path)">
                <CollapsibleTrigger class="flex flex-row items-center justify-between w-full">
                    <span>{{ item.title }}</span>
                    <ChevronUp v-if="open" class="size-4" />
                    <ChevronDown v-else class="size-4" />
                </CollapsibleTrigger>
                <CollapsibleContent class="flex flex-col ml-4">
                    <NuxtLink v-for="child in item.children" :key="child.path" :to="child.path" activeClass="active" class="[&.active]:!text-primary transition-all flex flex-row items-center justify-between">
                        {{ child.title }}
                        <div class="flex flex-row gap-1 items-center">
                            <Badge v-for="tag in child.tags">{{ tag }}</Badge>
                        </div>
                    </NuxtLink>
                </CollapsibleContent>
            </Collapsible>
            <NuxtLink v-else :key="item.path" :to="item.path" activeClass="active" class="[&.active]:!text-primary transition-all flex flex-row items-center justify-between">
                {{ item.title }}
                <div class="flex flex-row gap-1 items-center">
                    <Badge v-for="tag in item.tags">{{ tag }}</Badge>
                </div>
            </NuxtLink>
        </template>
        <a v-if="COLLECTION_INFO[props.collection].repo" :href="COLLECTION_INFO[props.collection].repo" target="_blank" class="mt-auto flex flex-row items-center gap-2">
            <Github class="size-4" />
            {{ COLLECTION_INFO[props.collection].title }}
            {{ COLLECTION_INFO[props.collection].version || "" }}
            <ExternalLink class="size-4 ml-auto" />
        </a>
    </nav>
</template>
