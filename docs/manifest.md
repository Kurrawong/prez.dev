# Prez Manifest Model

A Prez Manifest is an RDF file that describes and links to a set of resources that can be loaded into an RDF database for Prez to provide access to.

This page defines the Prez Manifest specification and links to relevant tools.

1. [The model](#model)
2. [Manifest Resource Roles Vocabulary](#roles-vocabulary)
3. [Examples](#examples)
4. [Tools](#tools)

## Model

``` mermaid
graph LR
  Manifest --1:1-N--> Resource;
  Resource --1:1--> artifact;
  Resource --1:1--> role;
  Resource --1:0-1--> name;
  Resource --1:0-1--> decription;
  Resource --1:0-N--> conformsTo;
  artifact --1:0-1--> mainEntity;
  artifact --1:0-1--> contentLocation;
  artifact --1:0-N--> conformsTo;
```

### Rules

1. An instance of the Manifest class, `prez:Manifest`, MUST have 1 or more Resource Descriptors, `prof:ResourceDescriptor` instances, indicated by the `prof:hasResource` predicate. The Manifest instance can be identified by an IRI or a Blank Node.

2. Each Resource Descriptor MUST have at least one `prof:hasArtifact` predicate indicating either an RDF literal resource (a string) containing the location of the artifact or a Blank Node containing the location of the artifacts indicated by the `schema:contentLocation` predicate and the main artifact IRI within that content location indicated by `schema:mainEntity`.

3. Where content location is indicated, it MUST be a file path or path pattern relative to the manifest or a URL.

4. Each Resource Descriptor MUST also have exactly one `prof:hasRole` predicate indicating a Concept from the _Manifest Resource Roles Vocabulary_.

5. Each Resource Descriptor MAY have a `schema:name` and/or a `schema:description` predicate indicating literal resources naming and describing it.

6. A Resource, or an Artifact, MAY indicate that it (if an Artifact) or the Artifacts within it (if a Resource) conform to any number of defined Standards or Profiles of Standards, using the predicate `dcterms:conformsTo`.
    * Validators can be indicated either by using "well known" validator IRIs or by directly indicating the validator RDF file
          * current "well known" are listed below and can be indicated using an IRI like this:
              * `dcterms:conformsTo <WELL-KNONW-VALIDATOR-IRI> ;`
          * other validators, such as `my-local-validator.ttl` or `http://online-validator.com/val.ttl` should be indicated using a literal, like this: 
              * `dcterms:conformsTo "path/from/manifest/root/to/my-local-validator.ttl" ;`

#### Known Validators

The following validators can be referred to by IRI, as described above:

| *Validator*           | *IRI*                                              | *Scope*                                             |
|-----------------------|----------------------------------------------------|-----------------------------------------------------|
| GeoSPARQL             | `<http://www.opengis.net/def/geosparql/validator>` | Spatial Objects                                     |
| IDN Catalogue Profile | `<https://data.idnau.org/pid/cp/validator>`        | Catalogued resources containing Indigenous metadata |
| VocPub                | `<https://w3id.org/profile/vocpub>`                | Vocabularies                                        |

### Validation

Prez Manifests themselves can be validated using a [SHACL](https://www.w3.org/TR/shacl/) validation tool, using this validator file below:

```
--8<-- "docs/assets/validator.ttl"
```

!!! note

    The `prezmanifest` tool, described [below](#prezmanifest) has a simple validate function that tests a manifest with this validator and also checks that all the artifacts indicated in resources actually exist.

<a id="roles-vocabulary"></a>

## Manifest Resource Roles Vocabulary

This roles vocabulary contains the allowed Roles that a Resource can play with respect to a Manifest.

The IRI of this vocabulary is:

* `https://prez.dev/ManifestResourceRoles`
    * the vocab namespace is `https://prez.dev/ManifestResourceRoles/`
    * recommended namespace prefix is `mrr`

Human-readable form:

| Concept IRI                                | Label                                  | Definition                                                                                                           | Parent                          |
|--------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------|
| `mrr:CatalogueData`                        | Catalogue Data                         | Data for the catalogue, usually a Catalogue, including the identity of it and each item fo resource                  | -                               |
| `mrr:ResourceData`                         | Resource Data                          | Data for the resource of the catalogue                                                                               | -                               |
| `mrr:CatalogueAndResourceModel`            | Catalogue & Resource Model             | The default model for the catalogue and the resource. Must be a set of SHACL Shapes                                  | -                               |
| `mrr:CatalogueModel`                       | Catalogue Model                        | The default model for the catalogue. Must be a set of SHACL Shapes                                                   | `mrr:CatalogueAndResourceModel` |
| `mrr:ResourceModel`                        | Resource Model                         | The default model for the resource. Must be a set of SHACL Shapes                                                    | `mrr:CatalogueAndResourceModel` |
| `mrr:CompleteCatalogueAndResourceLabels`   | Complete Resource & Catalogue Labels   | All the labels - possibly including names, descriptions & seeAlso links - for the Catalogue and Resource objects     | -                               |
| `mrr:IncompleteCatalogueAndResourceLabels` | Incomplete Resource & Catalogue Labels | Some of the labels - possibly including names, descriptions & seeAlso links - for the Catalogue and Resource objects | -                               |

Machine-readable form:

```
--8<-- "docs/assets/mrr.ttl"
```

The IRI for automatic retrieval of this vocabulary file is: <https://prez.dev/ManifestResourceRoles>.

## Examples

### Valid

A simple, valid, Manifest.

```
--8<-- "docs/assets/manifest.ttl"
```

### Invalid - no role

The second Resource Descriptor does not indicate a role as it is commented out.

```
--8<-- "docs/assets/manifest-invalid-01.ttl"
```

### Invalid - bad location

The third resource specifies an invalid location, the non-existent web address of https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttlx which has had an extra 'x' added at the end.

```
--8<-- "docs/assets/manifest-invalid-03.ttl"
```

### `mainEntity` use

A snippet of a Manifest - just one value for `hasResource` - showing use of `mainEntity` and `contentLocation` instead of just a literal file path.

```
    [
        prof:hasArtifact
            [
                schema:contentLocation "vocabs/image-test.ttl" ;
                schema:mainEntity <https://example.com/demo-vocabs/image-test> ;
            ] ,
            "vocabs/language-test.ttl" ;
        prof:hasRole mrr:ResourceData ;
        schema:description "skos:ConceptScheme objects in RDF (Turtle) files in the vocabs/ folder" ;
        schema:name "Resource Data"
    ] ,
```

### conformance claim - single

A single artifact claiming conformance to the [VocPub Profile of SKOS](https://w3id.org/profile/vocpub).

```
    prof:hasArtifact
        [
            schema:contentLocation "vocabs/image-test.ttl" ;
            schema:mainEntity <https://example.com/demo-vocabs/image-test> ;
            dcterms:conformsTo <https://w3id.org/profile/vocpub> ;
        ] ,
```

### conformance claim - all

A single Resource in a Manifest claiming conformance to the [VocPub Profile of SKOS](https://w3id.org/profile/vocpub) for all artifacts (there are 3 given).

```
    [
        prof:hasArtifact
            [
                schema:contentLocation "vocabs/image-test.ttl" ;
                schema:mainEntity <https://example.com/demo-vocabs/image-test> ;
            ] ,
            "vocabs/language-test.ttl" ;
            "vocabs/other-vocab.ttl" ;
        prof:hasRole mrr:ResourceData ;
        # ...
        dcterms:conformsTo <https://w3id.org/profile/vocpub> ;
    ] ,
```

### conformance claim - supplied validator

To indicate a validator stored in a local file, `my-local-validator.ttl`:

```
    [
        prof:hasArtifact
            [
                schema:contentLocation "vocabs/image-test.ttl" ;
                schema:mainEntity <https://example.com/demo-vocabs/image-test> ;
            ] ,
            "vocabs/language-test.ttl" ;
            "vocabs/other-vocab.ttl" ;
        prof:hasRole mrr:ResourceData ;
        # ...
        dcterms:conformsTo "path/to/my-local-validator.ttl" ;
    ] ,
```

## Tools

### prezmanifest

The `prezmanifest` command line tool and Python package, available at https://github.com/Kurrawong/prez-manifest and on [PyPI](https://pypi.org/project/prezmanifest/), provides a number of functions to work with Prez Manifests. The functions provided are:

* **validate**
    * performs SHACL validation on the Manifest, followed by existence checking for each resource - are they reachable by this script on the file system or over the Internet? Will also check any [Conformance Claims](#conformance-claims)given in the Manifest)
* **label**
    * lists all the IRIs for elements with a Manifest's Resources that don't have labels. Given a source of additional labels, such as the [KurrawongAI Semantic Background](#kurrawongai-semantic-background), it can try to extract any missing labels and insert them into a Manifest as an additional labelling resource
* **document**
    * **table**: can create a Markdown or ASCCIIDOC table of Resources from a Prez Manifest file for use in README files in repositories
    * **catalogue**: add the IRIs of resources within a Manifest's 'Resource Data' object to a catalogue RDF file
* **load**
    *  extract all the content of all Resources listed in a Prez Manifest and load it into either a single RDF multi-graph ('quads') file or into an RDF DB instance by using the Graph Store Protocol

See the package's repository for installation and use details. 
