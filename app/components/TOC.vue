<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { TableOfContents } from "lucide-vue-next";
import type { TocLink } from "@nuxt/content";
import { cn } from "~/lib/utils";

const props = defineProps<{
    links: TocLink[];
    class?: HTMLAttributes["class"];
}>();

const router = useRouter();

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
                <TableOfContents class="size-4" />
            </Button>
        </SheetTrigger>
        <SheetContent side="right" class="p-2 m-4 rounded-md h-[calc(100dvh-75px)]] top-[75px]" hideClose>
            <SheetHeader class="flex flex-row justify-between items-center p-0">
                <SheetClose as-child>
                    <Button variant="ghost" size="icon">
                        <TableOfContents class="size-4" />
                    </Button>
                </SheetClose>
                <span class="text-sm">Page Contents</span>
                <div class="size-9"></div>
            </SheetHeader>
            <TOCContent :links="props.links" class="lg:hidden" />
        </SheetContent>
    </Sheet>
    <!-- desktop nav -->
    <div :class="cn('border-l overflow-y-auto p-3 hidden lg:flex lg:flex-col lg:w-[255px] min-h-full', props.class)">
        <span class="mb-4">Page Contents</span>
        <TOCContent :links="props.links" />
    </div>
</template>
