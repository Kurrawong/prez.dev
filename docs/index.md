![](assets/prez-logo.png)

## What is Prez?

Prez is a multi-part open source web application that publishes "profiles of Knowledge Graph data".

Prez is most commonly used to publish:

* lists of managed vocabularies
* catalogues of semantic resources
* spatial reference datasets
* Knowledge Graph models

The main parts of Prez are:

* [Prez UI](https://github.com/RDFLib/prez-ui)
* [Prez API](https://github.com/RDFLib/prez)
* an [SPARQL-compliant](https://www.w3.org/TR/sparql11-protocol/) graph database, such as [Fuseki](https://jena.apache.org/documentation/fuseki2/)

### Other Prez tools 

In addition to the main Prez elements listed above, there are a series of smaller tools - scripts - that can be used to prepare [Semantic Web](https://en.wikipedia.org/wiki/Semantic_web) for publication by Prez. The main one of these is:

* [Prez Manifest](https://github.com/Kurrawong/prezmanifest)
    * provides a series of functions to work with Knowledge Graph data within Prez 

### Namespace

This web address, `https://prez.dev/`, is also the namespace for the Prez Ontology - the Prez system's main data model.

## Show me

Here are some live instances of Prez online:

<a href="https://test.icsm.information.qld.gov.au/">
![ICSM Prez instance](assets/icsm.png){width=45%, align=left}
</a>

<a href="https://demo.dev.kurrawong.ai/catalogs">
![KurrawongAI's demo instance](assets/demo.png){width=45%}
</a>

<p>&nbsp;</p>

<a href="https://vocabularies.sarig.sa.gov.au/vocab">
![GSSA instance](assets/sarig.png){width=45%, align=left}
</a>

<a href="hhttps://portal.bdr.gov.au/catalogues">
![BDR instance](assets/bdr.png){width=45%}
</a>

## How can I get Prez?

While being open source, Prez is mostly maintained by [KurrawongAI](https://kurrawong.ai) who provide professional services to assist with its use, see the [Prez Docs](https://docs.kurrawong.ai/prez/).

You can still run Prez, the API, and any other smaller Prez fools yourself by understanding how it works - see details via the link above.

If you need help, you can [contact KurrawongAI](https://kurrawong.ai/contact) who can assist you.

## Data Models

Other than the software tools described above, there are also data models within Prez:

* [Prez Ontology](ont.md)
* [Prez Manifest Model](manifest.md)
    * [Prez Manifest Resource Roles vocabulary](mrr.md)
