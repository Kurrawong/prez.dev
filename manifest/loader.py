"""
This script creates an n-quads files containing the following by parsing a Prez Manifest:

 1. A Named Graph for each content item using the item's IRI as the graph IRI
 2. A Named Graph for the container either using the container's IRI as the graph IRI if given, or by making one up if a Blank Node
 3. All the triples in resources with roles mrr:completeContainerAndContentLabels & mrr:incompleteContainerAndContentLabels within a Named Graph with IRI <https://background>
 4. An Olis Virtual Graph, <https://olis.dev/VirtualGraph> object which is as an alias for all the Named Graphs from 1., 2. & 3.
 5. Entries in the System Graph - Named Graph with IRI <https://olis.dev/SystemGraph> - for each Real and the Virtual Graph

Run this script with the -h flag for more help, i.e. ~$ python documentor.py -h





docker run --rm --env=ADMIN_PASSWORD=admin --volume=/Users/nick/work/kurrawong/prez.dev/manifest/fuseki/configuration:/fuseki-base/configuration --volume=/Users/nick/work/kurrawong/prez.dev/manifest/fuseki/databases:/fuseki-base/databases -p 3030:3030 --name manifest-loader
secoresearch/fuseki:5.1.0
"""
import argparse
import httpx
from urllib.parse import ParseResult, urlparse
from pathlib import Path
import sys
from rdflib import Graph, Namespace
from rdflib import PROF, RDF, SDO, SKOS
from kurrawong.fuseki import upload_file

MRR = Namespace("https://prez.dev/ManifestResourceRoles/")

__version__ = "1.0.0"


def load(sparql_endpoint: str, manifest_file: Path):
    g = Graph().parse(manifest_file)

    with httpx.Client() as client:
        # ContentData
        p = None
        for s, o in g.subject_objects(PROF.hasResource):
            for o2 in g.objects(o, PROF.hasRole):
                if o2 == MRR.ContentData:
                    for o3 in g.objects(o, PROF.hasArtifact):
                        if not len(str(o3).split("*")) > 1:
                            p = manifest_file.parent / Path(str(o3))

                            data = Graph().parse(p)
                            for ng in data.subjects(RDF.type, SKOS.ConceptScheme):
                                ng = str(ng)

                            if ng is not None:
                                upload_file(sparql_endpoint, p, client, ng)
                        else:
                            glob_parts = str(o3).split("*")
                            p = manifest_file.parent / Path(glob_parts[0])
                            p = p.glob("*." + glob_parts[1])

        print(p)
        # upload_file()
    return True

def setup_cli_parser(args=None):
    def url_file_or_folder(input: str) -> ParseResult | Path:
        parsed = urlparse(input)
        if all([parsed.scheme, parsed.netloc]):
            return parsed
        path = Path(input)
        if path.is_file():
            return path
        if path.is_dir():
            return path
        raise argparse.ArgumentTypeError(
            f"{input} is not a valid input. Must be a file, folder or sparql endpoint"
        )

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
    load(Path("/Users/nick/work/kurrawong/demo-vocabs/manifest.ttl"))
    exit()
    retval = cli(sys.argv[1:])
    if retval is not None:
        sys.exit(retval)