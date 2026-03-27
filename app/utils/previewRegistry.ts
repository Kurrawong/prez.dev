import NodePreview from "@/components/preview/NodePreview.vue";
import NodeContent from "@/components/preview/NodePreview.vue?raw";

export const PREVIEW_REGISTRY = {
    "node": {
        component: NodePreview,
        raw: NodeContent,
    },
};
