# Prez Manifest Model

A Prez Manifest is an RDF file that describes and links to a set of resources that can be loaded into an RDF database for Prez to provide access to.

To support Manifest creation and use, the following tools are provides:

1. [The model](#model)
2. [Manifest Resource Roles Vocabulary](#roles-vocabulary)
3. [Validator](#validator)
4. [Build Scripts](#build-scripts)
5. [Examples](#examples)

## Model

``` mermaid
graph LR
  Manifest --1:1-N--> Resource;
  Resource --1:1--> artifact;
  Resource --1:1--> role;
  Resource --1:0-1--> name;
  Resource --1:0-1--> decription;
```

The Manifest Model is simply a Manifest class, `prez:Manifest`, which MUST have 1 or more Resource Descriptors, `prof:ResourceDescriptor` indicated by the `prof:hasResource` predicate. 

Each Resource Descriptor MUST have exactly one `prof:hasArtifact` predicate indicating an RDF literal resource (string) giving a file path or path pattern containing the resource information, relative to the manifest.

Each Resource Descriptor MUST also have exactly one `prof:hasRole` predicate indicating a Concept from the _Manifest Resource Roles Vocabulary_.

Each Resource Descriptor MAY have a `schema:name` and/r a `schema:description` predicate indicating literal resources naming and describing it.

<a id="roles-vocabulary"></a>
## Manifest Resource Roles Vocabulary

This roles vocabulary contains the allowed roles that a resource can play with respect to a Manifest.

The IRI of this vocabulary is:

* `https://prez.dev/ManifestResourceRoles`
    * the vocab namespace is `https://prez.dev/ManifestResourceRoles/`
    * recommended namespace prefix is `mrr`

Human-readable form:

| Concept IRI                               | Label                                   | Definition                                                                                                          | Parent                         |
|-------------------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------|
| `mrr:ContainerData`                       | Container Data                          | Data for the container, usually a Catalogue, including the identity of it and each item fo content                  | -                              |
| `mrr:ContentData`                         | Content Data                            | Data for the content of the container                                                                               | -                              |
| `mrr:ContainerAndContentModel`            | Container & Content Model               | The default model for the container and the content. Must be a set of SAHCL Shapes                                  | -                              |
| `mrr:ContainerModel`                      | Container Model                         | The default model for the container. Must be a set of SAHCL Shapes                                                  | `mrr:containerAndContentModel` |
| `mrr:ContentModel`                        | Content Model                           | The default model for the content. Must be a set of SAHCL Shapes                                                    | `mrr:containerAndContentModel` |
| `mrr:CompleteContainerAndContentLabels`   | Complete Content and Container Labels   | All the labels - possibly indluding names, descriptions & seeAlso links - for the Container and Content objects     | -                              |
| `mrr:IncompleteContainerAndContentLabels` | Incomplete Content and Container Labels | Some of the labels - possibly indluding names, descriptions & seeAlso links - for the Container and Content objects | -                              |

Machine-readable form:

```
--8<-- "manifest/mrr.ttl"
```

--8<-- "mrr.ttl"

The IRI for automatic retrieval of this vocabulary file is: <https://prez.dev/ManifestResourceRoles>.


## Validator

This simple [SHACL](https://www.w3.org/TR/shacl/) validator "Shapes" file can be used by SHACL validation software to test the validity of a Manifest RDF file with respect to this model:

```
--8<-- "manifest/validator.ttl"
```

The IRI for automatic retrieval of this Shapes file is: <https://prez.dev/manifest/validator>.

The recommended tools to perform validation using this Shapes file are:

1. [KurrawongAI's Online Validator](https://tools.dev.kurrawong.ai/validate) - this Shapes file is pre-loaded
2. [pySHACL Python tool](https://pypi.org/project/pyshacl/) - for scripted validation

## Build Scripts

### Documentor

The `documentor.py` Python script in this documentation's repository creates a "Prez Resources" table in either Markdown or ASCIIDOC from a Manifest file which it validates first:

* <https://github.com/Kurrawong/prez.dev/blob/main/manifest/documentation.py>

#### Use
```
usage: documentor.py [-h] [-v] [-t {markdown,asciidoc}] input

positional arguments:
  input                 File, Folder or Sparql Endpoint to read RDF from

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -t {markdown,asciidoc}, --type {markdown,asciidoc}
                        The type of markup you want to export: Markdown or ASCCIDOC
```

#### Example

Using the first example Manifest, `example01.ttl` in this too's repository and also given in the [Example](#examples) section below:

```
~$ python documentor.py example01.ttl
```

produces:

```
Resource | Role | Description
--- | --- | ---
Catalogue Definition, [`catalogue.ttl`](catalogue.ttl) | [Container Data](https://prez.dev/ManifestResourceRoles/ContainerData) | The definition of, and medata for, the container which here is a dcat:Catalog object
Content, [`vocabs/*.ttl`](vocabs/*.ttl) | [Content Data](https://prez.dev/ManifestResourceRoles/ContentData) | skos:ConceptsScheme objects in RDF (Turtle) files in the vocabs/ folder
Profile Definition, [`ogc_records_profile.ttl`](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Container & Content Model](https://prez.dev/ManifestResourceRoles/ContainerAndContentModel) | The default Prez profile for Records API
Labels file, [`_background/labels.ttl`](_background/labels.ttl) | [Complete Content and Container Labels](https://prez.dev/ManifestResourceRoles/CompleteContainerAndContentLabels) | An RDF file containing all the labels for the container content

```

which renders as:

| Resource                                                                                                                                       | Role                                                                                                              | Description                                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Catalogue Definition, [`catalogue.ttl`](catalogue.ttl)                                                                                         | [Container Data](https://prez.dev/ManifestResourceRoles/ContainerData)                                            | The definition of, and medata for, the container which here is a dcat:Catalog object |
| Content, [`vocabs/*.ttl`](vocabs/*.ttl)                                                                                                        | [Content Data](https://prez.dev/ManifestResourceRoles/ContentData)                                                | skos:ConceptsScheme objects in RDF (Turtle) files in the vocabs/ folder              |
| Profile Definition, [`ogc_records_profile.ttl`](https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttl) | [Container & Content Model](https://prez.dev/ManifestResourceRoles/ContainerAndContentModel)                      | The default Prez profile for Records API                                             |
| Labels file, [`_background/labels.ttl`](_background/labels.ttl)                                                                                | [Complete Content and Container Labels](https://prez.dev/ManifestResourceRoles/CompleteContainerAndContentLabels) | An RDF file containing all the labels for the container content                      |

### Loader

==_In Progress_==

The `loader.py` Python script in this documentation's repository creates a 

* <https://github.com/Kurrawong/prez.dev/blob/main/manifest/loader.py>

## Examples

See the simple and always up-to-date [KurrawongAI Demo Vocabularies manifest](https://github.com/Kurrawong/demo-vocabs/manifest.ttl):

Full:
```
--8<-- "manifest/example01.ttl"
```

Partial:
```
--8<-- "manifest/example02.ttl"
```

Invalid (second Resource Descriptor does not indicate a role)
```
--8<-- "manifest/example03.ttl"
```