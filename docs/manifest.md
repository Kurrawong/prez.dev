# Prez Manifest Model

A Prez Manifest is an RDF file that describes and links to a set of resources that can be loaded into an RDF database for Prez to provide access to.

This pase defines the Prez Manifest specification and links to relevant tools.

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

**Valid**:

```
--8<-- "docs/assets/manifest.ttl"
```

**Invalid** - second Resource Descriptor does not indicate a role as it is commented out

```
--8<-- "docs/assets/manifest-invalid-01.ttl"
```

**Invalid** - the third resource specifies an invalid location, the non-existent web address of https://github.com/RDFLib/prez/blob/main/prez/reference_data/profiles/ogc_records_profile.ttlx which has had an extra 'x' added at the end.

```
--8<-- "docs/assets/manifest-invalid-03.ttl"
--8<-- "docs/assets/manifest-invalid-03.ttl"
```

## Tools

The `prez-manifest` Python package, available at https://github.com/Kurrawong/prez-manifest, provides a number of functions to to work with Prez Manifests. The functions provided are:

* `create_table`: creates an ASCIIDOC or Markdown table of Manifest content from a Manifest file
* `validate`: validates that a Manifest file conforms to the specification and that all linked-to assets are available
* `load`: loads a Manifest file, and all the resources it specifies, into either an n-quads file or a Fuseki database

See the package's repository for details. 
