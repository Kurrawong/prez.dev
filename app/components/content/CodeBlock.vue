<script lang="ts" setup>
import type { HTMLAttributes } from "vue";
import { Copy } from "lucide-vue-next";
import { cn } from "~/lib/utils";

const props = defineProps<{
    lang?: string;
    class?: HTMLAttributes["class"];
}>();

const slots = useSlots();

function copyToClipboard() {
    navigator.clipboard.writeText(slots.default!().map(c => c.children).join("\n"))
}
</script>

<template>
    <pre :lang="props.lang" :class="cn('group relative !m-0', props.class)">
<slot /><Button variant="ghost" size="icon" class="z-10 absolute hidden group-hover:flex top-2 right-2" title="Copy to clipboard" @click="copyToClipboard"><Copy class="size-4" /></Button>
</pre>
</template>
