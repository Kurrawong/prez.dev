<script lang="ts" setup>
import { ArrowRight, ExternalLink } from "lucide-vue-next";

const route = useRoute();

useHead({
    title: "Prez Docs"
});

const { data: page } = await useAsyncData(route.path, () => {
    return queryCollection("home").path(route.path).first();
});

const { data: navigation } = await useAsyncData("home-navigation", () => {
    return queryCollectionNavigation("home");
});
</script>

<template>
    <div class="grow max-w-[1400px] mx-auto w-full">
        <main>
            <div v-if="route.path === '/'" class="w-full min-h-[400px] flex items-center justify-center dark:bg-gradient-to-b dark:from-0% dark:from-tertiary/50 dark:to-60% dark:to-background p-6">
                <div class="grid grid-cols-1 md:grid-cols-[1fr_3fr] gap-4">
	                <div class="flex justify-center">
		                <img src="/img/prez-logo.png" alt="Prez logo" class="h-36 md:h-auto aspect-square" />
	                </div>
	                <Card class="min-h-48 bg-background/50 backdrop-blur-md">
	                    <CardContent class="flex flex-col justify-between h-full items-start">
		                    <h1 class="text-3xl">Presenting Linked Data</h1>
		                    <p class="text-muted-foreground">A highly customisable suite of tools...</p>
		                    <div class="flex flex-row justify-between w-full">
			                    <Button as-child>
				                    <NuxtLink to="/quickstart">
					                    Quickstart
					                    <ArrowRight />
				                    </NuxtLink>
			                    </Button>
			                    <Button variant="outline" as-child>
				                    <a href="https://demo.dev.kurrawong.ai" target="_blank">
					                    See the demo
					                    <ExternalLink />
				                    </a>
			                    </Button>
		                    </div>
	                    </CardContent>
	                </Card>
                </div>
            </div>
	        <div class="w-full mb-4 py-1 flex">
		        <nav class="px-2 flex flex-row items-stretch justify-between md:items-center mx-auto w-full max-w-lg">
			        <Button v-for="link in navigation" :key="link.path" :variant="route.path === link.path ? 'secondary' : 'ghost'" asChild>
				        <NuxtLink
					        :to="link.path"
				        >
					        {{ link.title }}
				        </NuxtLink>
			        </Button>
		        </nav>
	        </div>
            <Breadcrumbs v-if="route.path !== '/'" :page="page" collection="home" class="px-2" />
            <ContentRenderer v-if="page" :value="page" class="prose dark:prose-invert max-w-full p-2" />
        </main>
    </div>
</template>
