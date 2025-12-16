<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { Sidebar as SidebarIcon } from "lucide-vue-next";
import type { PageCollections } from "@nuxt/content";
import { cn } from "~/lib/utils";

const router = useRouter();

const props = defineProps<{
    collection: Exclude<keyof PageCollections, "home">;
    class?: HTMLAttributes["class"];
}>();

const showSidenav = ref(false);

router.beforeEach((from, to) => {
    showSidenav.value = false;
});
</script>

<template>
    <!-- mobile nav -->
    <Sheet v-model:open="showSidenav">
        <SheetTrigger as-child>
            <Button variant="ghost" size="icon" :class="cn('lg:hidden', props.class)">
                <SidebarIcon class="size-4" />
            </Button>
        </SheetTrigger>
        <SheetContent side="left" class="p-2" hideClose>
            <SheetHeader class="flex flex-row justify-between items-center p-2">
                <SheetClose as-child>
                    <Button variant="ghost" size="icon">
                        <SidebarIcon class="size-4" />
                    </Button>
                </SheetClose>
                <NuxtLink :to="`/${props.collection}`" class="text-lg font-semibold">{{ COLLECTION_INFO[props.collection].title }}</NuxtLink>
                <div class="size-9"></div>
            </SheetHeader>
            <SidebarContent :collection="props.collection" class="lg:hidden" />
        </SheetContent>
    </Sheet>
    <!-- desktop nav -->
    <div :class="cn('border-r overflow-y-auto p-2 hidden lg:flex lg:w-[240px]', props.class)">
        <SidebarContent :collection="props.collection" />
    </div>
</template>
