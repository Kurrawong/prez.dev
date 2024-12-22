"""
This script creates an n-quads files containing the following by parsing a Prez Manifest:

 1. A Named Graph for each resource using the item's IRI as the graph IRI
 2. A Named Graph for the catalogue, either using the catalogue's IRI as the graph IRI + "-catalogue" if given, or by making one up - a Blank Node
 3. All the triples in resources with roles mrr:CompleteCatalogueAndResourceLabels & mrr:IncompleteCatalogueAndResourceLabels within a Named Graph with IRI <https://background>
 4. An Olis Virtual Graph, <https://olis.dev/VirtualGraph> object using the catalogue IRI, if give, which is as an alias for all the Named Graphs from 1., 2. & 3.
 5. Multiple entries in the System Graph - Named Graph with IRI <https://olis.dev/SystemGraph> - for each Named and the Virtual Graph from 1., 2. & 3.

Optionally this scrit can upload the n-quads file to a SPARQL endpoint.

Run this script with the -h flag for more help, i.e. ~$ python loader.py -h
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

import httpx
from rdflib import DCAT, DCTERMS, PROF, RDF, SDO, SKOS
from rdflib import Graph, URIRef, Dataset

from ns_mrr import MRR
from ns_olis import OLIS
from validator import validate
from kurrawong.format import make_quads
from kurrawong.utils import load_graph

__version__ = "1.0.0"


def export_quads(
    g: Graph, dataset_iri: URIRef, destination_path: Optional[Path] = None
):
    d = make_quads(g, dataset_iri)
    d.bind("reg", "http://purl.org/linked-data/registry#")
    d.bind("olis", OLIS)

    if destination_path is not None:
        if destination_path.is_file():
            d2 = Dataset()
            d2.parse(destination_path)
            d3 = d + d2
            d3.serialize(format="trig", destination=destination_path)
        else:
            d.serialize(format="trig", destination=destination_path)
    else:
        print(d.serialize(format="trig"))


def load(
    manifest: Path,
    sparql_endpoint: str = None,
    export_quads_file: Path = None,
):
    """Loads a catalogue of data from a manifest file, whose content are valid according to the Prez Manifest Model
    (https://kurrawong.github.io/prez.dev/manifest/) either into a specified quads file in the Trig format, or into a
    given SPARQL Endpoint."""

    if sparql_endpoint is not None and export_quads_file is not None:
        raise ValueError("You may only specify either a sparql_endpoint or a export_quads_file, not both")
    elif sparql_endpoint is None and export_quads_file is None:
        raise ValueError("You must specify either a sparql_endpoint or a export_quads_file, not neither")

    # load and validate manifest
    g = validate(manifest)

    MANIFEST_ROOT_DIR = manifest.parent

    vg = Graph()
    vg_iri = None

    with (httpx.Client() as http_client):
        for s, o in g.subject_objects(PROF.hasResource):
            for role in g.objects(o, PROF.hasRole):
                # The catalogue - must be processed first
                if role == MRR.CatalogueData:
                    for artifact in g.objects(o, PROF.hasArtifact):
                        # load the Catalogue, determine the Virtual Graph & Catalogue IRIs
                        # and fail if we can't see a Catalogue object
                        c = load_graph(MANIFEST_ROOT_DIR / str(artifact))
                        vg_iri = c.value(predicate=RDF.type, object=DCAT.Catalog)
                        if vg_iri is None:
                            raise ValueError(
                                f"ERROR: Could not create a Virtual Graph as no Catalog found in the Catalogue data"
                            )
                        catalogue_iri = URIRef(str(vg_iri) + "-catalogue")

                        # add to the System Graph
                        vg.add((vg_iri, RDF.type, OLIS.VirtualGraph))
                        vg.add((vg_iri, OLIS.isAliasFor, catalogue_iri))
                        vg_name = c.value(
                            subject=vg_iri,
                            predicate=SDO.name | DCTERMS.title | SKOS.prefLabel,
                        ) or str(vg_iri)
                        vg.add((vg_iri, SDO.name, vg_name))

                        # export the Catalogue data
                        if export_quads_file is not None:
                            export_quads(c, catalogue_iri, export_quads_file)
                        else:
                            pass

        # non-catalogue resources
        for s, o in g.subject_objects(PROF.hasResource):
            for role in g.objects(o, PROF.hasRole):
                # The data files & background - must be processed after Catalogue
                if role in [
                    MRR.CompleteCatalogueAndResourceLabels,
                    MRR.IncompleteCatalogueAndResourceLabels,
                    MRR.ResourceData,
                    ]:

                    for artifact in g.objects(o, PROF.hasArtifact):
                        if not len(str(artifact).split("*")) > 1:
                            files = [manifest.parent / Path(str(artifact))]
                        else:
                            glob_parts = str(artifact).split("*")
                            files = Path(
                                manifest.parent / Path(glob_parts[0])
                            ).glob("*" + glob_parts[1])

                        for f in files:
                            fg = Graph().parse(f)
                            if role == MRR.ResourceData:
                                resource_iri = fg.value(
                                    predicate=RDF.type, object=SKOS.ConceptScheme
                                )

                            if role in [MRR.CompleteCatalogueAndResourceLabels,
                                          MRR.IncompleteCatalogueAndResourceLabels]:
                                resource_iri = URIRef("http://background")

                            vg.add((vg_iri, OLIS.isAliasFor, resource_iri))
                            export_quads(fg, resource_iri, export_quads_file)

        # export the System Graph
        if export_quads_file is not None:
            export_quads(vg, OLIS.SystemGraph, export_quads_file)
        else:
            pass

    return True


def setup_cli_parser(args=None):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="{version}".format(version=__version__),
    )

    parser.add_argument(
        "-e",
        "--endpoint",
        help="The SPARQL endpoint you want to load the data into",
        required=True,
    )

    parser.add_argument(
        "manifest",
        help="A manifest file to process",
        type=argparse.FileType("r"),
        required=True,
    )

    return parser.parse_args(args)


def cli(args=None):
    if args is None:
        args = sys.argv[1:]

    args = setup_cli_parser(args)

    #
    #   Do stuff here
    #


if __name__ == "__main__":
    manifest = Path(__file__).parent / "tests" / "demo-vocabs" / "manifest.ttl"
    results_file = Path(__file__).parent / "results.trig"
    print()
    print(load(manifest, export_quads_file=results_file, sparql_endpoint="x"))
    exit()
    retval = cli(sys.argv[1:])
    if retval is not None:
        sys.exit(retval)
