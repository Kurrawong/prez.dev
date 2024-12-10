from kurrawong.fuseki import upload_file
from pathlib import Path
import httpx


def test_file_upload_ng_replacement():
    SPARQL_ENDPOINT = "http://localhost:3030/mani"
    minimalist_rdf = Path(__file__).parent / "minimal.ttl"
    with httpx.Client() as client:
        upload_file(
            SPARQL_ENDPOINT,
            minimalist_rdf,
            client,
            "https://example.com/demo-vocabs/language-test3"
        )