# Prez Manifest Model

A Prez Manifest is an RDF file that describes and links to a set of resources that can be loaded into an RDF database for Prez to provide access to.

This page defines the Prez Manifest specification and links to relevant tools.

1. [The model](#model)
2. [Manifest Resource Roles Vocabulary](#roles-vocabulary)
3. [Examples](#examples)
4. [Tools](#tools)

## Model

### Overview

``` mermaid
graph LR
  style Manifest fill:#FF90BB,stroke:#666,stroke-width:2px
  Manifest --1:1-N--> ResourceDescriptor;
  style ResourceDescriptor fill:#FFC1DA,stroke:#666,stroke-width:2px
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px 
  ResourceDescriptor --1:1-N--> artifact;
  ResourceDescriptor --1:1--> hasRole;
  ResourceDescriptor --1:0-N--> conformsTo;
  ResourceDescriptor --1:0-1--> additionalType;
  ResourceDescriptor --1:0-1--> sync;
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px  
  artifact --1:0-N--> conformsTo;
  artifact --1:0-1--> additionalType;
  artifact --1:0-1--> sync;
  artifact --1:0-1--> mainEntity;
  artifact --1:0-1--> contentLocation;
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px  
  artifact --1:0-1--> dateModified;
  artifact --1:0-1--> versionIRI;
  artifact --1:0-1--> version;
```

_See [Annex A: Diagram Breakdown](#annex-a-diagram-breakdown) below for a part-by-part explanation of this diagram._

## Rules

1. An instance of the Manifest class, `prez:Manifest`, MUST have 1 or more Resource Descriptors, `prof:ResourceDescriptor` instances, indicated by the `prof:hasResource` predicate. The Manifest instance can be identified by an IRI or a Blank Node.

2. Each Resource Descriptor MUST have at least one `prof:hasArtifact` predicate indicating either an RDF literal resource (a string) containing the location of the artifact or a Blank Node containing the location of the artifacts indicated by the `schema:contentLocation` predicate and the main artifact IRI within that content location indicated by `schema:mainEntity`.
    * See the [Main Entity](#main-entity) details below

3. Where content location is indicated, it MUST be a file path or path pattern relative to the manifest or a URL.

4. Each Resource Descriptor MUST also have exactly one `prof:hasRole` predicate indicating a Concept from the [Manifest Resource Roles Vocabulary](mrr.md).

5. Each Resource Descriptor MAY have a `schema:name` and/or a `schema:description` predicate indicating literal resources naming and describing it.

6. A Resource, or an Artifact, MAY indicate that it (if an Artifact) or the Artifacts within it (if a Resource) conform to any number of defined Standards or Profiles of Standards, using the predicate `dcterms:conformsTo`.
    * Validators can be indicated either by using "well known" validator IRIs or by directly indicating the validator RDF file
          * current "well known" are listed below and can be indicated using an IRI like this:
              * `dcterms:conformsTo <WELL-KNONW-VALIDATOR-IRI> ;`
          * other validators, such as `my-local-validator.ttl` or `http://online-validator.com/val.ttl` should be indicated using a literal, like this: 
              * `dcterms:conformsTo "path/from/manifest/root/to/my-local-validator.ttl" ;`
    * See the [Known Validators](#known-validators) list below

7. A Resource, or an Artifact, MAY indicate that it (if an Artifact) or the Artifacts within it (if a Resource) is of a specific class, using the predicate `schema:additionalType`
    * See the [Known Classes](#known-classes) list below
8. A Resource, or an Artifact, MAY indicate that it should not be ignored by synchronisation tooling by setting a predicate `prez:sync` to `false`
    * See the [Indicating no action](#indicating-no-action) section below
9. An Artifact may have "versioning information" about it indicated by use of a number of known versioning predicates
    * see the [Artifact Versioning](#artifact-versioning) section below

#### Known Validators

The following validators can be referred to by IRI, as described above:

| *Validator*           | *IRI*                                              | *Scope*                                             |
|-----------------------|----------------------------------------------------|-----------------------------------------------------|
| GeoSPARQL             | `<http://www.opengis.net/def/geosparql/validator>` | Spatial Objects                                     |
| IDN Catalogue Profile | `<https://data.idnau.org/pid/cp/validator>`        | Catalogued resources containing Indigenous metadata |
| VocPub                | `<https://w3id.org/profile/vocpub>`                | Vocabularies                                        |

#### Known Classes

Some classes of resource are commonly catalogued and, when they are, their class does not need to be indicated within a Manifest. These classes are:

* `dcat:Resource`
* `dcat:Dataset`
* `dcat:Catalog`
* `owl:Ontology`
* `schema:CreativeWork`
* `schema:Dataset`
* `schema:DataCatalog`
* `skos:ConceptScheme`

If an Artifact, or all the Artifacts within a Resource, are not one of these types, then they can be indicated as being so by use of `schema:additionalType` like this:

```turtle
[]
    a prez:Manifest ;
    prof:hasResource
        # ...
        [
            prof:hasArtifact "resources/*.ttl" ;
            prof:hasRole mrr:ResourceData ;
            schema:additionalType <{A-CLASS-IRI}> ;
        ] ,
        # ...
.
```

This will allow the Manifest to communicate the class of the object software should be looking for within the resource.

#### Main Entity

If, for some reason, a resource is neither of one of the Known Classes nore it its class able to be indicated with `schema:additionalType`, the specific IRI of the resource can be indicated using `schema:mainEntity`. This may be needed in situations where an RDF file containing a resource also contains multiple other instance of the same class.

```turtle
[]
    a prez:Manifest ;
    prof:hasResource
        # ...
        [
            prof:hasArtifact "resources/file1.ttl" ;
            prof:hasRole mrr:ResourceData ;
            schema:mainEntity <{RESOURCE-IRI}> ;
        ] ,
        # ...
.
```

#### Indicating no action

If a Manifest wishes to list a resource but indicate it not for automatic handling by manifest tooling - perhaps it's too large to synchronise with an RDF DB - then the predicate `prez:sync` with the value `false` should be set.

Here is an example of a Manifest indicating 4 spatial datasets, one of which is too large to sync:

```turtle
[]
    a prez:Manifest ;
    prof:hasResource
        [
            prof:hasArtifact "resources/*.ttl" ;  # datset1.ttl, dataset2.ttl & dataset3.ttl
            prof:hasRole mrr:ResourceData ;
        ] ,
        [
            prof:hasArtifact "resources/large/dataset4.ttl" ;
            prof:hasRole mrr:ResourceData ;
            prez:sync false ;
        ] ;
.        
```

### Artifact versioning

An Artifact's version may be indicated by use of any or all of the following predicates:

* `owl:versionIRI`
* `schema:version` or `owl:versionInfo`
* `schema:dateModified` or `dcterms:modified`

If this is done, then tools, such as _prezmanifest_ that load and sync Manifest-described data, can obtain versioning information from a Manifest file, rather than by inspecting Artifacts' contents.

## Validation

The validator - a file containing rules - for Manifests is given in [Annex B: Manifest Validator](#annex-b-manifest-validator) below.

A manifest and all its content can also be validated using the _prezmanifest_ tool's _validate_ function which both validates a Manifest file using the validator below and also any content for which a _conformance claim_ is given.

See the [Tools](#tools) section below for info on the _prezmanifest_ tool.

Additionally, any stand-alon SHACL validator can also be used to validate a Manifest. Again, see the tools section below.

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

### additionalType

Where a 

## Tools

### prezmanifest - [GitHub](https://github.com/Kurrawong/prez-manifest), [PyPI](https://pypi.org/project/prezmanifest/)

The _prezmanifest_ command line tool and Python package, available on [GitHub](https://github.com/Kurrawong/prez-manifest) and on [PyPI](https://pypi.org/project/prezmanifest/), provides a number of functions to work with Prez Manifests. The functions provided are:

* **validate** - validate a Manifest file and contents
* **label** - check Manifest contents for unlabelled elements
* **document** - create certain forms of documentation
* **load** - load a Manifest's content into a file or DB
* **sync** - synchronise a Manifest's contents with a DB

See the package's repository for installation and use details. 

### SHACL validation

The preferred way to perform validation of a Prez Manifest file is to use the _prezmanifest_ tool's _validate_ function, as listed above. Hoever, you can also perform validation of a manifest - the manifest file only, not the content it refers to, using any one of a number of [SHACL](https://www.w3.org/TR/shacl/) validators. 

See these notes for a listing of general-purpose SHACL validation tools:

* [ABIS standard's notes on SHACL tooling & validation](https://linked.data.gov.au/def/abis#_performing_validation)

## Annex A: Diagram Breakdown

### `Manifest` & `ResourceDescriptor`

``` mermaid
graph LR
  style Manifest fill:#FF90BB,stroke:#666,stroke-width:2px
  Manifest --1:1-N--> ResourceDescriptor;
  style ResourceDescriptor fill:#FFC1DA,stroke:#666,stroke-width:2px
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px 
  ResourceDescriptor --1:1-N--> artifact;
  subgraph main
  ResourceDescriptor --1:1--> hasRole;
  ResourceDescriptor --1:0-N--> conformsTo;
  ResourceDescriptor --1:0-1--> additionalType;
  ResourceDescriptor --1:0-1--> sync;
  end
```

A `Manifest` must indicate _at least one_ `ResourceDescriptor`.

`ResourceDescriptor` instances MUST have the predicates of:

* `hasRole` - exactly 1
* `hasArtifact`- at least 1

`ResourceDescriptor` instances MAY have the predicates of:

* `conformsTo` - at most 1
* `additionalType` - at most 1
* `sync` - at most 1. If present, value must be `false`, e.g. `true` is default

### `Artifact` - description

``` mermaid
graph LR
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px  
```

``` mermaid
graph LR
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px  
  subgraph main
  artifact --1:0-N--> conformsTo;
  artifact --1:0-1--> additionalType;
  artifact --1:0-1--> sync;
  end
  subgraph artifact-only
  artifact --1:0-1--> mainEntity;
  artifact --1:0-1--> contentLocation;
  end
```

The value for the `hasArtifact` predicate can be either:

* a literal, with no further predicates of its own
* a node (likely a Blank Node) 

If a node, it MUST have:

* `contentLocation` - exactly 1
* `mainEntity` - exactly 1

If a node, it MAY have:

* `conformsTo` - at most 1
* `additionalType` - at most 1
* `sync` - at most 1. If present, value must be `false`, e.g. `true` is default

### `Artifact` - versioning

If a node, an `Artifact` MAY have:

* `dateModified` - at most 1
* `versionIRI` - at most 1
* `version` - at most 1

``` mermaid
graph LR
  style artifact fill:#F8F8E1,stroke:#666,stroke-width:2px  
  subgraph versioning
  artifact --1:0-1--> dateModified;
  artifact --1:0-1--> versionIRI;
  artifact --1:0-1--> version;
  end
```

## Annex B: Manifest Validator

```
--8<-- "docs/assets/validator.ttl"
```