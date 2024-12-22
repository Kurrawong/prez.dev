from manifest.loader import load
from pathlib import Path


def test_load_01():
    manifest = Path(__file__).parent / "demo-vocabs" / "manifest.ttl"
    results_file = Path(__file__).parent / "results.trig"
    print()
    print(load(manifest, sparql_endpoint=None, export_quads_file=results_file))
