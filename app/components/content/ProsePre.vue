<script setup lang="ts">
import type {HTMLAttributes} from "vue";
import {cn} from "~/lib/utils";

const props = withDefaults(defineProps<{
	code?: string;
	language?: string;
	filename?: string;
	highlights?: number[];
	meta?: string;
	class?: HTMLAttributes["class"];
}>(), {
	code: "",
	highlights: () => [],
});
</script>

<template>
	<ClientOnly v-if="props.language === 'mermaid'">
		<Mermaid >
			<slot />
		</Mermaid>
	</ClientOnly>
	<div v-else class="flex flex-col border rounded-md my-6">
		<div v-if="props.filename" class="p-2">{{props.filename}}</div>
		<pre :class="cn('!my-0 whitespace-pre-wrap', props.class)"><slot /></pre>
	</div>
</template>

<style>
pre code .line {
	//display: block;
}
</style>