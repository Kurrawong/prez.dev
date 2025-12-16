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
        title: "Prez UI",
        repo: "https://github.com/RDFLib/prez-ui",
        version: "4.2.0",
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
        title: "Prez API",
        repo: "https://github.com/RDFLib/prez",
        version: "4.23.2",
        icons: {
            "/prez": Home,
            "/prez/development": Code,
            "/prez/deployment": Rocket,
            "/prez/configuration": Wrench,
            "/prez/quickstart": Play,
        }
    },
    prezmanifest: {
        title: "Prez Manifest",
        repo: "https://github.com/Kurrawong/prezmanifest",
        version: "1.0.14",
        icons: {
            "/prezmanifest": Home,
            "/prezmanifest/development": Code,
            "/prezmanifest/quickstart": Play,
        }
    },
};