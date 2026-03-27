import type { PageCollections } from "@nuxt/content";
import {ArrowUpCircle, Code, Home, type LucideIcon, Palette, Play, Rocket, Wrench} from "lucide-vue-next";

export const COLLECTION_INFO: Record<keyof PageCollections, {
    title: string;
    repo?: string;
    version?: string;
    icons?: Record<string, LucideIcon>;
}> = {
    home: {
        title: "Home",
    },
    prezui: {
        title: "PrezUI",
        repo: "https://github.com/RDFLib/prez-ui",
        version: "4.3.0",
        icons: {
            "/prezui": Home,
            "/prezui/theming": Palette,
            "/prezui/upgrade": ArrowUpCircle,
            "/prezui/development": Code,
            "/prezui/deployment": Rocket,
            "/prezui/configuration": Wrench,
            "/prezui/quickstart": Play,
        }
    },
    prez: {
        title: "PrezAPI",
        repo: "https://github.com/RDFLib/prez",
        version: "4.23.6",
        icons: {
            "/prezapi": Home,
            "/prezapi/development": Code,
            "/prezapi/deployment": Rocket,
            "/prezapi/configuration": Wrench,
            "/prezapi/quickstart": Play,
        }
    },
    prezmanifest: {
        title: "KG Manifest",
        repo: "https://github.com/Kurrawong/kgmanifest",
        version: "1.2.1",
        icons: {
            "/kgmanifest": Home,
            "/kgmanifest/development": Code,
            "/kgmanifest/quickstart": Play,
        }
    },
};