<script lang="ts" setup>
import { Sun, Moon, SunMoon, Menu } from "lucide-vue-next";

const colorMode = useColorMode();
const router = useRouter();
const route = useRoute();

const showSidenav = ref(false);

const collections = Object.keys(COLLECTION_INFO);

const currentCollection = computed(() => {
    if (route.path === "/") {
        return "home";
    } else {
        const firstPath = route.path.split("/")[1];
        if (collections.includes(firstPath)) {
            return firstPath;
        } else {
            return "home";
        }
    }
});

router.beforeEach((from, to) => {
    showSidenav.value = false;
});
</script>

<template>
    <header class="flex flex-row items-center gap-2 p-2 bg-tertiary text-tertiary-foreground">
        <!-- mobile nav -->
        <Sheet v-model:open="showSidenav">
            <SheetTrigger as-child>
                <Button variant="ghost" size="icon" class="md:hidden">
                    <Menu class="size-4" />
                </Button>
            </SheetTrigger>
            <SheetContent side="top" class="p-2" hideClose>
                <SheetHeader class="flex flex-row justify-between items-center p-2">
                    <SheetClose as-child>
                        <Button variant="ghost" size="icon">
                            <Menu class="size-4" />
                        </Button>
                    </SheetClose>
                    <NuxtLink to="/" class="flex flex-row gap-1 items-center mr-auto">
                        <img src="/img/prez-logo.png" alt="Prez logo" class="w-[60px]">
                        <span class="font-semibold text-2xl">Prez</span>
                    </NuxtLink>
                    <div class="size-9"></div>
                </SheetHeader>
                <TopnavContent class="md:hidden" />
            </SheetContent>
        </Sheet>
        <NuxtLink to="/" class="flex flex-row gap-1 items-center mr-auto">
            <img src="/img/prez-logo.png" alt="Prez logo" class="w-[60px]">
            <span class="font-semibold text-2xl">Prez</span>
        </NuxtLink>
        <!-- desktop nav -->
        <TopnavContent class="hidden md:flex" />
        <div class="flex flex-row items-center gap-2">
            <SearchCommand :collection="currentCollection" />
            <Button variant="ghost" size="icon" @click="!colorMode.unknown ? colorMode.value === 'dark' ? colorMode.preference = 'light' : colorMode.preference = 'dark' : undefined">
                <SunMoon v-show="colorMode.unknown" class="size-4" />
                <Sun v-show="colorMode.value === 'dark'" class="size-4" />
                <Moon v-show="colorMode.value === 'light'" class="size-4" />
            </Button>
        </div>
    </header>
</template>
