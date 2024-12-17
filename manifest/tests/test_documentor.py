import pytest
from rdflib import Graph
from pathlib import Path
from manifest.documentor import create_table
from textwrap import dedent


def test_create_table_01():
    expected = dedent("""
        Resource | Role | Description
        --- | --- | ---
        Catalogue Definition, [`catalogue.ttl`](catalogue.ttl) | [Container Data](https://prez.dev/ManifestResourceRoles/ContainerData) | The definition of, and medata for, the container which here is a dcat:Catalog object
        Content Data, [`vocabs/*.ttl`](vocabs/*.ttl) | [Content Data](https://prez.dev/ManifestResourceRoles/ContentData) | skos:ConceptsScheme objects in RDF (Turtle) files in the vocabs/ folder
        Profile Definition, [`ogc_records_profile.ttl`](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Container & Content Model](https://prez.dev/ManifestResourceRoles/ContainerAndContentModel) | The default Prez profile for Records API
        Labels, [`_background/labels.ttl`](_background/labels.ttl) | [Complete Content and Container Labels](https://prez.dev/ManifestResourceRoles/CompleteContainerAndContentLabels) | An RDF file containing all the labels for the container content                
        """).strip()

    g = Graph().parse(Path(__file__).parent / "demo-vocabs" / "manifest.ttl")

    result = create_table(g)

    print()
    print()
    print(expected)
    print()
    print()
    print(result)
    print()
    print()

    assert result == expected


def test_create_table_02():
    expected = dedent("""
        Resource | Role | Description
        --- | --- | ---
        Catalogue Definition, [`catalogue.ttl`](catalogue.ttl) | [Container Data](https://prez.dev/ManifestResourceRoles/ContainerData) | The definition of, and medata for, the container which here is a dcat:Catalog object
        Content, [`vocabs/*.ttl`](vocabs/*.ttl) | [Content Data](https://prez.dev/ManifestResourceRoles/ContentData) | skos:ConceptsScheme objects in RDF (Turtle) files in the vocabs/ folder
        Profile Definition, [`ogc_records_profile.ttl`](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Container & Content Model](https://prez.dev/ManifestResourceRoles/ContainerAndContentModel) | The default Prez profile for Records API
        Labels file, [`_background/labels.ttl`](_background/labels.ttl) | [Complete Content and Container Labels](https://prez.dev/ManifestResourceRoles/CompleteContainerAndContentLabels) | An RDF file containing all the labels for the container content                
        """).strip()

    g = Graph().parse(Path(__file__).parent / "demo-vocabs" / "manifest-invalid-01.ttl")

    with pytest.raises(ValueError):
        create_table(g)
