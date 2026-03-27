import { type MimeType } from "h3";

function acceptQualities(acceptHeader: string): Record<MimeType, number> {
    return acceptHeader.split(",").reduce((obj, curr) => {
        const [m, q] = curr.split(";q=");
        obj[m] = q ? Number(q) : 1;
        return obj;
    }, {} as Record<MimeType, number>);
}

function getQuality(mimetype: MimeType, qualities: Record<MimeType, number>): number {
    const type = mimetype.split("/")[0];
    switch (true) {
        case mimetype in qualities:
            return qualities[mimetype];
        case `${type}/*` in qualities:
            return qualities[`${type}/*`];
        case "*/*" in qualities:
            return qualities["*/*"];
        default:
            return 0;
    }
}

export default defineEventHandler(async (event) => {
    if (getRequestURL(event).pathname === "/") {
        const headers = getRequestHeaders(event);
        const { _mediatype } = getQuery(event);
        const qualities = acceptQualities(headers["accept"] || "");
        if (
            (_mediatype && _mediatype === "text/turtle") ||
            (headers["accept"] && getQuality("text/turtle", qualities) > getQuality("text/html", qualities))
        ) {
            const storage = useStorage();
            const turtleData = await storage.getItem("assets:server:rdf.ttl");
            setResponseHeaders(event, {
                "content-type": "text/turtle",
            });
            return turtleData;
        }
    }
});
