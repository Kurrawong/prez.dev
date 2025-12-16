import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    compatibilityDate: "2025-07-15",
    devtools: { enabled: true },
    modules: ["@nuxt/content", "@nuxtjs/color-mode", "shadcn-nuxt"],
    css: [
        "prez-components/prez-components.css",
        "@kurrawongai/kai-ui/kai-ui.css",
        "~/assets/css/tailwind.css",
        "~/assets/css/style.css"
    ],
    vite: {
        plugins: [
            tailwindcss(),
        ],
    },
    content: {
        build: {
            markdown: {
                highlight: {
                    theme: {
                        default: "light-plus",
                        dark: "dark-plus",
                    }
                },
            }
        }
    },
    colorMode: {
        classPrefix: "",
        classSuffix: "",
    },
    shadcn: {
        prefix: "",
        componentDir: "./app/components/ui"
    }
});