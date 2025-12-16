<script lang="ts" setup>
import { Node } from "prez-components";
import { node, literal } from "prez-lib";

const term = node({
    value: "https://example.com",
    label: literal("Prez node")
});
</script>

<template>
    <Node :term="term" />
</template>
