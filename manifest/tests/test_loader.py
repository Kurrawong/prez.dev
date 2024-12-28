from manifest.loader import load
from pathlib import Path
from rdflib import Dataset, URIRef


def test_load_01():
    manifest = Path(__file__).parent / "demo-vocabs" / "manifest.ttl"
    results_file = Path(__file__).parent / "results.trig"

    load(manifest, sparql_endpoint=None, export_quads_file=results_file)

    # load the resultant Dataset to test it
    d = Dataset()
    d.parse(results_file, format="trig")

    graph_ids = [x.identifier for x in d.graphs()]

    assert URIRef("https://example.com/demo-vocabs-catalogue") in graph_ids
    assert URIRef("https://example.com/demo-vocabs/image-test") in graph_ids
    assert URIRef("https://example.com/demo-vocabs/language-test") in graph_ids
    assert URIRef("http://background") in graph_ids
    assert URIRef("https://olis.dev/SystemGraph") in graph_ids

    Path(results_file).unlink()