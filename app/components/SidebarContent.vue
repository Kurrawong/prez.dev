<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import type { PageCollections } from "@nuxt/content";
import {ChevronDown, ChevronUp, Github, ExternalLink, File, ChevronRight} from "lucide-vue-next";
import { cn } from "~/lib/utils";

const route = useRoute();

const props = defineProps<{
	collection: Exclude<keyof PageCollections, "home">;
    class?: HTMLAttributes["class"];
}>();

const { data } = await useAsyncData(`${props.collection}-navigation`, () => {
	return queryCollectionNavigation(props.collection, ["tags"]);
});
</script>

<template>
    <nav :class="cn('flex flex-col grow gap-1 overflow-y-auto', props.class)">
        <template v-for="item in data?.[0].children">
            <Collapsible v-if="item.children" class="group/collapsible" :defaultOpen="route.path.startsWith(item.path)">
	            <CollapsibleTrigger class="flex flex-row items-center justify-between w-full" asChild>
		            <Button variant="ghost" size="sm" class="[&.active]:bg-accent/50 justify-start">
			            <component v-if="COLLECTION_INFO[props.collection].icons?.[item.path]" :is="COLLECTION_INFO[props.collection].icons[item.path]" />
			            <File v-else />
			            <span>{{ item.title }}</span>
			            <ChevronRight class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-90" />
		            </Button>
	            </CollapsibleTrigger>
                <CollapsibleContent class="flex flex-col ml-4 px-2 py-1 gap-1 border-l">
	                <Button v-for="child in item.children" :key="child.path" variant="ghost" size="sm" class="[&.active]:bg-accent/50 justify-start" asChild>
		                <NuxtLink :to="child.path" activeClass="active" class="">
			                <span>{{ child.title }}</span>
			                <div class="flex flex-row gap-1 items-center ml-auto">
				                <Badge v-for="tag in child.tags">{{ tag }}</Badge>
			                </div>
		                </NuxtLink>
	                </Button>
                </CollapsibleContent>
            </Collapsible>
	        <Button v-else variant="ghost" size="sm" class="[&.active]:bg-accent/50 justify-start" asChild>
		        <NuxtLink :key="item.path" :to="item.path" activeClass="active" class="">
			        <component v-if="COLLECTION_INFO[props.collection].icons?.[item.path]" :is="COLLECTION_INFO[props.collection].icons[item.path]" />
			        <File v-else />
			        <span>{{ item.title }}</span>
			        <div class="flex flex-row gap-1 items-center ml-auto">
				        <Badge v-for="tag in item.tags">{{ tag }}</Badge>
			        </div>
		        </NuxtLink>
	        </Button>
        </template>
    </nav>
</template>
