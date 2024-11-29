"""
This script creates a "Prez Resources" table in either Markdown or ASCIIDOC from a Manifest file which it validates first

Run this script with the -h flag for more help, i.e. ~$ python documentor.py -h
"""

import argparse
from pyshacl import validate
from urllib.parse import ParseResult, urlparse
from pathlib import Path
import sys
from rdflib import Graph
from rdflib import PROF, SDO, SKOS

__version__ = "1.0.0"


def create_table(g: Graph, t="markdown") -> str:
    if t == "asciidoc":
        header = "|===\n| Resource | Role | Description\n\n"
    else:
        header = "Resource | Role | Description\n--- | --- | ---\n"

    body = ""
    for s, o in g.subject_objects(PROF.hasResource):
        a = str(g.value(o, PROF.hasArtifact))
        if t == "asciidoc":
            artifact = f'link:{a}[`{a.split("/")[-1] if a.startswith("http") else a}`]'
        else:
            artifact = f'[`{a.split("/")[-1] if a.startswith("http") else a}`]({a})'
        role_iri = g.value(o, PROF.hasRole)
        role_label = g.value(role_iri, SKOS.prefLabel)
        if t == "asciidoc":
            role = f"{role_iri}[{role_label}]"
        else:
            role = f"[{role_label}]({role_iri})"
        name = g.value(o, SDO.name)
        description = g.value(o, SDO.description)
        n = f"{name}, {artifact}" if name is not None else f"{artifact}"
        d = description if description is not None else ""
        if t == "asciidoc":
            body += f"| {n} | {role} | {d}\n"
        else:
            body += f"{n} | {role} | {d}\n"

    if t == "asciidoc":
        footer = "|===\n"
    else:
        footer = ""

    return header + body + footer


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
        "-t",
        "--type",
        help="The type of markup you want to export: Markdown or ASCCIDOC",
        choices=["markdown", "asciidoc"],
        default="markdown",
    )

    parser.add_argument(
        "input",
        help="File, Folder or Sparql Endpoint to read RDF from",
        type=url_file_or_folder,
    )

    return parser.parse_args(args)


def cli(args=None):
    if args is None:
        args = sys.argv[1:]

    args = setup_cli_parser(args)

    # parse the target file
    g = Graph().parse(args.input)

    # add in the Roles vocab
    g.parse(Path(__file__).parent / "mrr.ttl")

    # validate it before proceeding
    valid, validation_graph, validation_text = validate(g, shacl_graph=str(Path(__file__).parent / "manifest-validator.ttl"))
    if not valid:
        txt = "Your Manifest is not valid:"
        txt += "\n\n"
        txt += validation_text
        raise ValueError(txt)

    print(create_table(g, t=args.type))


if __name__ == "__main__":
    retval = cli(sys.argv[1:])
    if retval is not None:
        sys.exit(retval)