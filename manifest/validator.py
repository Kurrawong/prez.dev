"""Validate a manifest file

~$ python validate.py {MANIFEST_FILE_PATH}"""

import sys
from pathlib import Path
from pyshacl import validate
from rdflib import Graph
from rdflib.namespace import PROF, RDF, RDFS
import httpx


def main(mainfest_file_path: Path) -> bool:
    ME = Path(__file__)

    # SHACL validation
    manifest_graph = Graph().parse(mainfest_file_path)
    data_graph = manifest_graph + Graph().parse(ME.parent / "mrr.ttl")
    valid, v_graph, v_text = validate(data_graph, shacl_graph=str(ME.parent / "validator.ttl"))

    if not valid:
        raise ValueError(f"SHACL invalid:\n\n{v_text}")

    # Content link validation
    for s, o in manifest_graph.subject_objects(PROF.hasResource):
        for o2 in manifest_graph.objects(o, PROF.hasArtifact):
            resource_relative_path = str(o2)
            if "http" in resource_relative_path:
                r = httpx.get(resource_relative_path)
                if 200 <= r.status_code < 400:
                    pass
                else:
                    raise ValueError(f"Remote content link non-resolving: {resource_relative_path}")
            elif "*" in resource_relative_path:
                glob_parts = resource_relative_path.split("*")
                dir = Path(mainfest_file_path.parent / Path(glob_parts[0]))
                if not Path(dir).is_dir():
                    raise ValueError(f"The content link {resource_relative_path} is not a directory")
            else:
                # It must be a local
                RESOURCE_PATH = Path(mainfest_file_path.parent / o2)
                if not RESOURCE_PATH.is_file():
                    print(f"Content link {RESOURCE_PATH} is invalid - not a file")

    return True


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())