<script lang="ts" setup>
import { Editor } from "@kurrawongai/kai-ui";
import type { Slot, VNode, VNodeArrayChildren } from "vue";

type EditorProps = InstanceType<typeof Editor>["$props"];

const props = defineProps<{
    lang?: EditorProps["language"];
    content: string;
}>();

const colorMode = useColorMode();

// const slotRef = useTemplateRef("slotRef")

// const slots = useSlots();

// const defaultSlotContent = slots.default!()[0].children.default!()[0].children;
// const defaultSlotContent = extractSlotContent(slots.default!()).join("");
// console.log(slots.default().map(x => typeof x.children === "string" ? x.children : x.children.default()))
// console.log(slots.default().map(x => typeof x.children === "string" ? x.children : (Array.isArray(x) ? x.children?.map(y => y.children) : x.children)))

// function extractSlotContent(d: VNode[]): string[] {
//     const content: string[] = [];
//     d.forEach((s, i) => {
//         // console.log(s.textContent)
//         if (typeof s.children === "string") {
//             // console.log("string")
//             content.push(s.children);
//         } else if (Array.isArray(s.children)) {
//             // console.log("array")
//             content.push(...extractSlotContent(s.children));
//         } else {
//             // console.log("object")
//             content.push(...extractSlotContent(s.children?.default()));
//         }
//     });

//     return content;
// }

const editorConfig: EditorProps["options"] = {
    // lineNumbers: false,
};

// const getSlotChildrenText = children => children.map(node => {
//   if (!node.el.textContent || typeof node.el.textContent === 'string') return node.el.textContent || ''
//   else if (Array.isArray(node.el.textContent)) return getSlotChildrenText(node.el.textContent)
//   else if (node.el.textContent.default) return getSlotChildrenText(node.el.textContent.default())
// }).join('')


// const slotTexts = slots.default && getSlotChildrenText(slots.default()) || ''
// console.log(slotTexts)

// console.log($slots.default().innerHTML)

// console.log(slotRef.value)
</script>

<template>
    <Tabs>
        <TabsList>
            <TabsTrigger value="preview">
                Preview
            </TabsTrigger>
            <TabsTrigger value="editor">
                Code
            </TabsTrigger>
        </TabsList>
        <TabsContent value="preview">

        </TabsContent>
        <TabsContent value="editor">
            <Editor
                readonly
                :options="editorConfig"
                :modelValue="props.content"
                :language="props.lang"
                hideLanguage
                hideDownloadButton
                :theme="colorMode.value"
            />
        </TabsContent>
    </Tabs>
</template>
