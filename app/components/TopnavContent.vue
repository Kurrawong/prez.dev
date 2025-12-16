<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { ExternalLink } from "lucide-vue-next";
import { cn } from "~/lib/utils";

const props = defineProps<{
    class?: HTMLAttributes["class"];
}>();

const route = useRoute();

const links = Object.entries(COLLECTION_INFO).map(([k, v]) => ({path: k === "home" ? "/" : `/${k}`, title: v.title}));

function isActive(link: { path: string; title: string; }): boolean {
    if (route.path === link.path) {
        return true;
    } else {
        if (link.path === "/" && !Object.keys(COLLECTION_INFO).includes(route.path.split("/")[1])) { // in home collection
            return true;
        } else {
            return route.path.startsWith(link.path + "/");
        }
    }
}
</script>

<template>
    <nav :class="cn('flex flex-col md:flex-row items-stretch md:items-center', props.class)">
        <NuxtLink
            v-for="link in links"
            :key="link.path"
            :to="link.path"
            :class="`hover:text-primary [&.active]:text-primary [&.active]:hover:text-primary md:[&.active]:text-primary-foreground md:[&.active]:border-b-primary border-b-[1px] border-b-transparent mt-[1px] px-2 py-1 transition-all ${isActive(link) ? 'active' : ''}`"
        >
            {{ link.title }}
        </NuxtLink>
	    <Button variant="ghost" class="border" as-child>
		    <a target="_blank" href="https://demo.dev.kurrawong.ai">Demo <ExternalLink class="size-4" /></a>
	    </Button>
    </nav>
</template>
