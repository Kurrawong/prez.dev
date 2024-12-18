"""Validate a manifest file

~$ python validate.py {MANIFEST_FILE_PATH}"""

import sys
from pathlib import Path
from typing import Union

import httpx
from kurrawong.utils import load_graph
from pyshacl import validate as shacl_validate
from rdflib.namespace import PROF


def validate(manifest: Path) -> bool:
    ME = Path(__file__)

    # SHACL validation
    manifest_graph = load_graph(manifest)
    mrr_vocab_graph = load_graph(ME.parent / "mrr.ttl")
    data_graph = manifest_graph + mrr_vocab_graph
    shacl_graph = load_graph(ME.parent / "validator.ttl")
    valid, v_graph, v_text = shacl_validate(data_graph, shacl_graph=shacl_graph)

    if not valid:
        raise ValueError(f"SHACL invalid:\n\n{v_text}")

    # Content link validation
    for s, o in manifest_graph.subject_objects(PROF.hasResource):
        for artifact in manifest_graph.objects(o, PROF.hasArtifact):
            artifact_str = str(artifact)
            if "http" in artifact_str:
                r = httpx.get(artifact_str)
                if 200 <= r.status_code < 400:
                    pass
                else:
                    raise ValueError(
                        f"Remote content link non-resolving: {artifact_str}"
                    )
            elif "*" in artifact_str:
                glob_parts = artifact_str.split("*")
                dir = Path(manifest.parent / Path(glob_parts[0]))
                if not Path(dir).is_dir():
                    raise ValueError(
                        f"The content link {artifact_str} is not a directory"
                    )
            else:
                # It must be a local
                if not (manifest.parent / artifact_str).is_file():
                    print(f"Content link {manifest.parent / artifact_str} is invalid - not a file")

    return manifest_graph


if __name__ == "__main__":
    validate(Path(sys.argv[1]).resolve())
