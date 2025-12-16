<script lang="ts" setup>
import { Editor } from "@kurrawongai/kai-ui";

const props = defineProps<{
    component: string;
}>();

const colorMode = useColorMode();
</script>

<template>
    <Tabs defaultValue="preview" class="border rounded-md">
        <TabsList class="bg-transparent">
            <TabsTrigger value="preview">
                Preview
            </TabsTrigger>
            <TabsTrigger value="editor">
                Code
            </TabsTrigger>
        </TabsList>
        <TabsContent value="preview">
            <div class="p-4 border flex items-center justify-center min-h-[400px]">
                <component :is="PREVIEW_REGISTRY[props.component].component" />
            </div>
        </TabsContent>
        <TabsContent value="editor">
            <Editor
                readonly
                :modelValue="PREVIEW_REGISTRY[props.component].raw"
                language="text"
                hideLanguage
                hideDownloadButton
                :theme="colorMode.value"
            />
        </TabsContent>
    </Tabs>
</template>
