# Manifest Resource Roles Vocabulary

This roles vocabulary contains the allowed `Roles` that a resource, described within a `ResourceDescriptor`, can play with respect to a `Manifest`.

## Identifier

The IRI of this vocabulary is:

* **`https://prez.dev/ManifestResourceRoles`**

The vocab namespace is `https://prez.dev/ManifestResourceRoles/`.
 
The recommended namespace prefix is `mrr`.

## Human-readable

The human-readable form of this vocabulary is as follows:

| Concept IRI                                | Label                                  | Definition                                                                                                           | Parent                          |
|--------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------|
| `mrr:CatalogueData`                        | Catalogue Data                         | Data for the catalogue, usually a Catalogue, including the identity of it and each item fo resource                  | -                               |
| `mrr:ResourceData`                         | Resource Data                          | Data for the resource of the catalogue                                                                               | -                               |
| `mrr:CatalogueAndResourceModel`            | Catalogue & Resource Model             | The default model for the catalogue and the resource. Must be a set of SHACL Shapes                                  | -                               |
| `mrr:CatalogueModel`                       | Catalogue Model                        | The default model for the catalogue. Must be a set of SHACL Shapes                                                   | `mrr:CatalogueAndResourceModel` |
| `mrr:ResourceModel`                        | Resource Model                         | The default model for the resource. Must be a set of SHACL Shapes                                                    | `mrr:CatalogueAndResourceModel` |
| `mrr:CompleteCatalogueAndResourceLabels`   | Complete Resource & Catalogue Labels   | All the labels - possibly including names, descriptions & seeAlso links - for the Catalogue and Resource objects     | -                               |
| `mrr:IncompleteCatalogueAndResourceLabels` | Incomplete Resource & Catalogue Labels | Some of the labels - possibly including names, descriptions & seeAlso links - for the Catalogue and Resource objects | -                               |

## Machine-readable

The machine-readable form of this vocabulary, in [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework)'s [Turtle](https://en.wikipedia.org/wiki/Turtle_(syntax)) syntax, is:

```
--8<-- "docs/assets/mrr.ttl"
```
