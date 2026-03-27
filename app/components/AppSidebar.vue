<script setup lang="ts">
import {ChevronRight, Github, File} from "lucide-vue-next";
import type {PageCollections} from "@nuxt/content";
import type {HTMLAttributes} from "vue";

const route = useRoute();

const props = defineProps<{
	collection: Exclude<keyof PageCollections, "home">;
	class?: HTMLAttributes["class"];
}>();

const { data } = await useAsyncData(`${props.collection}-navigation`, () => {
	return queryCollectionNavigation(props.collection, ["tags"]);
});
</script>

<template>
	<Sidebar class="h-full">
		<SidebarHeader>
			<SidebarMenu>
				<SidebarMenuItem class="flex flex-row items-center gap-2">
					<NuxtLink :to="`/${props.collection}`" class="flex flex-row items-center gap-1">
						<img src="/img/prez-logo.png" alt="Prez logo" class="w-6">
						<span class="">{{ COLLECTION_INFO[props.collection].title }}</span>
					</NuxtLink>
					<Badge v-if="COLLECTION_INFO[props.collection].version" variant="secondary">v{{ COLLECTION_INFO[props.collection].version }}</Badge>
					<Button v-if="COLLECTION_INFO[props.collection].repo" variant="ghost" size="icon" class="ml-auto" asChild>
						<a :href="COLLECTION_INFO[props.collection].repo" target="_blank">
							<Github class="size-4" />
						</a>
					</Button>
				</SidebarMenuItem>
			</SidebarMenu>
		</SidebarHeader>
		<SidebarContent>
			<SidebarGroup>
				<SidebarGroupContent>
					<SidebarMenu>
						<template v-for="item in data?.[0].children">
							<Collapsible v-if="item.children" class="group/collapsible" :defaultOpen="route.path.startsWith(item.path)">
								<SidebarMenuItem>
									<CollapsibleTrigger asChild>
										<SidebarMenuButton>
											<component v-if="COLLECTION_INFO[props.collection].icons?.[item.path]" :is="COLLECTION_INFO[props.collection].icons[item.path]" />
											<File v-else />
											<span>{{item.title}}</span>
											<ChevronRight class="ml-auto transition-transform group-data-[state=open]/collapsible:rotate-90" />
										</SidebarMenuButton>
									</CollapsibleTrigger>
									<CollapsibleContent>
										<SidebarMenuSub>
											<SidebarMenuSubItem v-for="child in item.children">
												<SidebarMenuSubButton :isActive="route.path === child.path" asChild>
													<NuxtLink :to="child.path">
														{{child.title}}
														<SidebarMenuBadge v-for="tag in child.tags">{{ tag }}</SidebarMenuBadge>
													</NuxtLink>
												</SidebarMenuSubButton>
											</SidebarMenuSubItem>
										</SidebarMenuSub>
									</CollapsibleContent>
								</SidebarMenuItem>
							</Collapsible>
							<SidebarMenuItem v-else>
								<SidebarMenuButton :isActive="route.path === item.path" asChild>
									<NuxtLink :to="item.path">
										<component v-if="COLLECTION_INFO[props.collection].icons?.[item.path]" :is="COLLECTION_INFO[props.collection].icons[item.path]" />
										<File v-else />
										<span>{{item.title}}</span>
										<SidebarMenuBadge v-for="tag in item.tags">{{ tag }}</SidebarMenuBadge>
									</NuxtLink>
								</SidebarMenuButton>
							</SidebarMenuItem>
						</template>
					</SidebarMenu>
				</SidebarGroupContent>
			</SidebarGroup>
		</SidebarContent>
	</Sidebar>
</template>