<script lang="ts" setup>
import type { PageCollections } from "@nuxt/content";
import { findPageBreadcrumb } from '@nuxt/content/utils'
import { COLLECTION_INFO } from "~/utils/consts";

const route = useRoute();

const props = defineProps<{
    collection: keyof PageCollections;
    page?: PageCollections[keyof PageCollections];
}>();

const { data: navigation } = await useAsyncData(`${props.collection}-navigation`, () => queryCollectionNavigation(props.collection));

const breadcrumbs = findPageBreadcrumb(navigation.value, route.path)
</script>

<template>
    <Breadcrumb>
        <BreadcrumbList class="p-0 list-none">
            <template v-if="props.page.path !== navigation?.[0].path">
                <BreadcrumbItem>
                    <BreadcrumbLink as-child>
                        <NuxtLink :to="navigation?.[0].path">{{ COLLECTION_INFO[props.collection].title }}</NuxtLink>
                    </BreadcrumbLink>
                </BreadcrumbItem>
                <BreadcrumbSeparator />
            </template>
            <template v-for="crumb in breadcrumbs">
                <template v-if="crumb.path !== navigation?.[0].path">
                    <BreadcrumbItem>
                        <BreadcrumbPage v-if="crumb.page === false">{{ crumb.title }}</BreadcrumbPage>
                        <BreadcrumbLink v-else as-child>
                            <NuxtLink :to="crumb.path">{{ crumb.title }}</NuxtLink>
                        </BreadcrumbLink>
                    </BreadcrumbItem>
                    <BreadcrumbSeparator />
                </template>
            </template>
            <BreadcrumbItem>
                <BreadcrumbPage>
                    {{ props.page.path === navigation?.[0].path ? COLLECTION_INFO[props.collection].title : props.page.title }}
                </BreadcrumbPage>
            </BreadcrumbItem>
        </BreadcrumbList>
    </Breadcrumb>
</template>
