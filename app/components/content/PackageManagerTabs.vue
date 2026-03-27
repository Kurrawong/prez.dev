<script lang="ts" setup>
const props = defineProps<{
  data: Record<string, string>;
}>();
</script>

<template>
    <Tabs :defaultValue="Object.keys(props.data)[0] || null" class="border rounded-md">
      <TabsList class="bg-transparent">
        <TabsTrigger v-for="manager in Object.keys(props.data)" :value="manager">{{ manager }}</TabsTrigger>
      </TabsList>
      <TabsContent v-for="(command, manager) in props.data" :value="manager">
        <CodeBlock lang="bash">{{ command }}</CodeBlock>
      </TabsContent>
    </Tabs>
</template>
