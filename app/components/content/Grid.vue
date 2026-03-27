<script setup lang="ts">
import type {HTMLAttributes} from "vue";
import {cn} from "~/lib/utils";

const props = defineProps<{
	cursor?: boolean;
	class?: HTMLAttributes["class"];
}>();

const applist = useTemplateRef("applist");

function onMouseMove(e: MouseEvent) {
	applist.value?.style.setProperty('--x', e.x + "px");
	applist.value?.style.setProperty('--y', e.y + "px");
}

if (props.cursor) {
	onMounted(() => {
		document.addEventListener("mousemove", onMouseMove);
	});

	onUnmounted(() => {
		document.removeEventListener("mousemove", onMouseMove);
	});
}
</script>

<template>
	<div ref="applist" :class="cn(`grid`, props.cursor ? 'applist' : '', props.class)">
		<slot />
	</div>
</template>

<style scoped>
.applist {
	--x: 0;
	--y: 0;
	--size: 10rem;
}
.applist:hover > * {
	background-size: cover;
	background-image: radial-gradient(
		circle at var(--x, 0) var(--y, 0),
		color-mix(in oklab, var(--color-primary) 80%, transparent),
		transparent var(--size)
	) !important;
	background-attachment: fixed;
}

.dark .applist:hover > * {
	background-size: cover;
	background-image: radial-gradient(
		circle at var(--x, 0) var(--y, 0),
		color-mix(in oklab, var(--color-primary) 50%, transparent),
		transparent var(--size)
	) !important;
	background-attachment: fixed;
}
</style>
