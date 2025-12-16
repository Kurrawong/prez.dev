<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { ExternalLink } from "lucide-vue-next";
import { cn } from "@/lib/utils";
import {NuxtLink} from "#components";

const props = withDefaults(defineProps<{
	class?: HTMLAttributes["class"];
	imgPosition?: "top" | "right" | "bottom" | "left";
	imgHalf?: boolean;
	to?: string;
}>(), {
	imgPosition: "right",
});
</script>

<template>
	<component
		:is="!!props.to ? (props.to.startsWith('/') ? NuxtLink : 'a') : 'div'"
		:to="!!props.to && props.to.startsWith('/') ? props.to : undefined"
		:href="!!props.to && !props.to.startsWith('/') ? props.to : undefined"
		:target="!!props.to && !props.to.startsWith('/') ? '_blank' : undefined"
		:class="cn(`bg-card text-card-foreground gap-6 rounded-xl border py-6 shadow-sm ${$slots.img ? `flex ${props.imgPosition === 'bottom' ? 'flex-col' : 'flex-col-reverse'} ${props.imgPosition === 'top' ? 'sm:flex-col-reverse' : (props.imgPosition === 'bottom' ? 'sm:flex-col' : (props.imgPosition === 'left' ? 'sm:flex-row-reverse' : 'sm:flex-row'))}` : ''}`, props.class)"
	>
		<div :class="props.imgHalf ? 'flex-1' : 'grow'">
			<CardHeader v-if="$slots.title || $slots.header" class="card-header">
				<slot name="header">
					<CardTitle v-if="$slots.title" class="font-normal text-xl inline-flex items-center gap-1">
						<slot name="title" mdc-unwrap="p" /><ExternalLink v-if="!!props.to && !props.to.startsWith('/')" class="size-5" />
					</CardTitle>
					<CardDescription v-if="$slots.description"><slot name="description" mdc-unwrap="p" /></CardDescription>
				</slot>
			</CardHeader>
			<CardContent :class="`card-body ${$slots.title || $slots.header ? '' : 'pt-6'}`">
				<slot />
			</CardContent>
			<CardFooter v-if="$slots.footer">
				<slot name="footer" mdc-unwrap="p" />
			</CardFooter>
		</div>
		<div v-if="$slots.img" :class="`flex shrink-0 justify-center items-center p-3 img ${props.imgHalf ? 'flex-1' : ''}`">
			<slot name="img" mdc-unwrap="p" />
		</div>
	</component>
</template>

<style scoped>
h3, :deep(h3) {
	margin: 0;
}

/* .card-header :deep(p) {
    margin: 0;
} */
.card-body > :deep(p:first-child) {
	margin-top: 0;
}
.card-body > :deep(p:last-child) {
	margin-bottom: 0;
}
.img :deep(img) {
	margin: 0;
}
</style>