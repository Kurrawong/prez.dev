<script lang="ts" setup>
import type { PageCollections } from "@nuxt/content";
import { Github, Code, Pencil } from "lucide-vue-next";

const route = useRoute();

const props = defineProps<{
    collection: Exclude<keyof PageCollections, "home">;
}>();

const { data: page } = await useAsyncData(route.path, () => {
    return queryCollection(props.collection).path(route.path).first();
});

useHead({
    titleTemplate: (titleChunk) => {
        let t = "Prez Docs";
        if (page.value) {
            t = `${COLLECTION_INFO[props.collection].title} | ${t}`;

            if (page.value.title !== COLLECTION_INFO[props.collection].title) {
                t = `${page.value.title} | ${t}`
            }
        }
        return t;
    }
});

function formatDate(date: string): string {
	const options: Intl.DateTimeFormatOptions = {
		day: "numeric",
		month: "long",
		year: "numeric",
	};
	return new Date(date).toLocaleDateString("en-AU", options);
}
</script>

<template>
    <div class="grid grid-cols-[max-content_1fr_max-content] grid-rows-[min-content_1fr] lg:grid-rows-1 grow gap-2 max-w-[1400px] mx-auto w-full">
        <Sidebar :collection="props.collection" />
        <div class="grow p-2 min-w-full row-start-2 col-span-full lg:row-start-1 lg:col-start-2 lg:col-span-1">
            <div class="flex flex-col">
                <Breadcrumbs :page="page" :collection="props.collection" />
                <div class="flex flex-row gap-4 items-center">
                    <h1 class="text-3xl mt-2 mb-4">{{ page.title }}</h1>
                    <div v-if="page.tags" class="flex flex-row gap-1 items-center">
                        <Badge v-for="tag in page.tags">{{ tag }}</Badge>
                    </div>
                </div>
                <p v-if="page.description">{{ page?.description }}</p>
                <div class="flex flex-row justify-between items-center gap-2">
                    <span class="flex flex-row items-center gap-1 text-sm text-muted-foreground" title="Last edited">
                        <template v-if="page?.date">
                            <Pencil class="size-4" /> {{ formatDate(page.date) }}
                        </template>
                    </span>
                    <div v-if="page.source || page.code" class="flex flex-row items-center gap-2">
                        <Button v-if="page.source" variant="outline" size="icon" as-child>
                            <a :href="page.source" target="_blank" title="Page source">
                                <Github class="size-4" />
                            </a>
                        </Button>
                        <Button v-if="page.code" variant="outline" size="icon" as-child>
                            <a :href="page.code" target="_blank" title="Component source code"><Code class="size-4" /></a>
                        </Button>
                    </div>
                </div>
            </div>
            <main class="prose dark:prose-invert">
                <ContentRenderer v-if="page" :value="page" />
            </main>
        </div>
        <TOC :links="page?.body.toc?.links || []" class="justify-self-end" />
    </div>
</template>
