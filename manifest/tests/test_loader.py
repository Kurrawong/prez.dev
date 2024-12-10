from manifest.loader import load
from pathlib import Path


def test_load_01():
    manifest = Path(__file__).parent / "manifest-01-valid.ttl"
    print(load("http://localhost:3030/mani/", manifest))


def test_load_02():
    manifest = Path(__file__).parent / "manifest-02-valid.ttl"
    print(load("http://localhost:3030/mani/", manifest))


