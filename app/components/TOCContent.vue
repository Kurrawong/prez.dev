<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import type { TocLink } from "@nuxt/content";
import { cn } from "~/lib/utils";

const props = defineProps<{
    links: TocLink[];
    class?: HTMLAttributes["class"];
}>();
</script>

<template>
    <div :class="cn('flex flex-col text-sm gap-2 toc-content', props.class)">
        <template v-for="link in props.links">
            <NuxtLink :to="`#${link.id}`" class="font-normal no-underline">{{ link.text }}</NuxtLink>
            <TOCContent v-if="link.children" :links="link.children" class="ml-4" />
        </template>
    </div>
</template>
