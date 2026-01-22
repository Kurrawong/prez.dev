<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import {Github, Sidebar as SidebarIcon} from "lucide-vue-next";
import type { PageCollections } from "@nuxt/content";
import { cn } from "~/lib/utils";
import SidebarContent from "~/components/SidebarContent.vue";

const router = useRouter();

const props = defineProps<{
    collection: Exclude<keyof PageCollections, "home">;
    class?: HTMLAttributes["class"];
}>();

const showSidenav = defineModel({default: false});

router.beforeEach((from, to) => {
    showSidenav.value = false;
});
</script>

<template>
    <!-- mobile nav -->
    <Sheet v-model:open="showSidenav">
<!--        <SheetTrigger as-child>-->
<!--            <Button variant="ghost" size="icon" :class="cn('md:hidden', props.class)">-->
<!--                <SidebarIcon class="size-4" />-->
<!--            </Button>-->
<!--        </SheetTrigger>-->
        <SheetContent side="left" class="p-2" hideClose>
            <SheetHeader class="flex flex-row justify-between items-center p-2">
                <SheetClose as-child>
                    <Button variant="ghost" size="icon">
                        <SidebarIcon class="size-4" />
                    </Button>
                </SheetClose>
<!--                <NuxtLink :to="`/${props.collection}`" class="text-lg font-semibold">{{ COLLECTION_INFO[props.collection].title }}</NuxtLink>-->
<!--                <div class="size-9"></div>-->
	            <NuxtLink :to="`/${props.collection}`" class="flex flex-row items-center gap-1">
		            <img src="/img/prez-logo.png" alt="Prez logo" class="w-6">
		            <span class="">{{ COLLECTION_INFO[props.collection].title }}</span>
	            </NuxtLink>
	            <Badge v-if="COLLECTION_INFO[props.collection].version" variant="secondary">v{{ COLLECTION_INFO[props.collection].version }}</Badge>
	            <Button v-if="COLLECTION_INFO[props.collection].repo" variant="ghost" size="icon" class="ml-auto" asChild>
		            <a :href="COLLECTION_INFO[props.collection].repo" target="_blank">
			            <Github class="size-4" />
		            </a>
	            </Button>
            </SheetHeader>
            <SidebarContent :collection="props.collection" class="md:hidden" />
        </SheetContent>
    </Sheet>
    <!-- desktop nav -->
    <div :class="cn('border-r p-2 hidden md:flex md:flex-col md:w-[240px] md:sticky md:top-0 md:self-start md:max-h-dvh', props.class)">
	    <div class="flex flex-row justify-between items-center gap-2">
		    <NuxtLink :to="`/${props.collection}`" class="flex flex-row items-center gap-1">
			    <img src="/img/prez-logo.png" alt="Prez logo" class="w-6">
			    <span class="">{{ COLLECTION_INFO[props.collection].title }}</span>
		    </NuxtLink>
		    <Badge v-if="COLLECTION_INFO[props.collection].version" variant="secondary">v{{ COLLECTION_INFO[props.collection].version }}</Badge>
		    <Button v-if="COLLECTION_INFO[props.collection].repo" variant="ghost" size="icon" class="ml-auto" asChild>
			    <a :href="COLLECTION_INFO[props.collection].repo" target="_blank">
				    <Github class="size-4" />
			    </a>
		    </Button>
	    </div>
	    <SidebarContent :collection="props.collection" />
    </div>
</template>
