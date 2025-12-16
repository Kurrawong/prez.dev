<script setup lang="ts">
import { Info, Lightbulb, MessageSquareWarning, TriangleAlert, OctagonAlert } from "lucide-vue-next";

const slots = useSlots();

function extractSlotContent(d: VNode[]): string[] {
    const content: string[] = [];
    d.forEach((s, i) => {
        if (typeof s.children === "string") {
            content.push(s.children);
        } else if (Array.isArray(s.children)) {
            content.push(...extractSlotContent(s.children));
        } else if ("default" in s.children) {
            content.push(...extractSlotContent(s.children?.default()));
        }
    });

    return content;
}

const alertMap = {
	"!NOTE": {
		title: "Note",
		icon: Info,
		borderColor: "border-[#1447e6] dark:border-[#1447e6]",
		textColor: "text-[#1447e6] dark:text-[#1447e6]",
	},
	"!TIP": {
		title: "Tip",
		icon: Lightbulb,
		borderColor: "border-[green]",
		textColor: "text-[green]",
	},
	"!IMPORTANT": {
		title: "Important",
		icon: MessageSquareWarning,
		borderColor: "border-[#ad46ff] dark:border-[#ad46ff]",
		textColor: "text-[#ad46ff] dark:text-[#ad46ff]",
	},
	"!WARNING": {
		title: "Warning",
		icon: TriangleAlert,
		borderColor: "border-[orange] dark:border-[#fe9a00]",
		textColor: "text-[orange] dark:text-[#fe9a00]",
	},
	"!CAUTION": {
		title: "Caution",
		icon: OctagonAlert,
		borderColor: "border-[#e7000b] dark:border-[#fb2c36]",
		textColor: "text-[#e7000b] dark:text-[#fb2c36]",
	},
};

const slotContent = computed(() => extractSlotContent(slots.default()));
const alertType = computed(() => slotContent.value[0].trim());
const isAlert = computed(() => alertType.value in alertMap);
</script>

<template>
	<Alert v-if="isAlert" :class="`my-4 ${alertMap[alertType].borderColor}`">
		<AlertTitle :class="`text-base flex flex-row items-center gap-2 ${alertMap[alertType].textColor}`">
			<component :is="alertMap[alertType].icon" class="size-4" />
			{{alertMap[alertType].title}}
		</AlertTitle>
		<AlertDescription class="text-base text-foreground inline *:last:mb-0">
			<template v-for="(c, i) in slots.default()">
				<p v-if="i === 0">
					<component :is="() => c.children.default().slice(1)" />
				</p>
				<component v-else :is="() => c" />
			</template>
		</AlertDescription>
	</Alert>
	<blockquote v-else>
		<slot />
	</blockquote>
</template>
