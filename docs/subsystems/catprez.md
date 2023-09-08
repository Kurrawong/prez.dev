_The [Prez](https://prez.dev) subsystem for cataloguing._

## What does CatPrez do?

CatPrez presents a [DCAT](https://www.w3.org/TR/vocab-dcat/) catalogue view of registered resources described using metadata. The resources can be any type of thing. Common types delivered by CatPrez are:

* **datasets** - digital data objects
* **documents** - important documents of various types
* **standards** - data and other standards with special relations to other standards
* **organisations** - listed with organisations metadata
* **projects** - with all the temporal and output information

...but you could have a catalogue of pets, boreholes, galactic clusters, whatever you like!

## What does it look like?

CatPrez presents several ways to access the content it contains:

A search page:

<figure markdown>
![](/assets/catprez-search.png)  
</figure>

A sortable & filterable listing:

<figure markdown>
![](/assets/catprez-listing.png)  
</figure>

Direct access to each object:

<figure markdown>
![](/assets/catprez-direct.png)  
</figure>

A specialised [OGC Rescords API](https://ogcapi.ogc.org/records/) technical interface:

<figure markdown>
![](/assets/catprez-ogcapi.png)
</figure>

A general-purpose [SPARQL](https://www.w3.org/TR/sparql11-protocol/) AP:

<figure markdown>
![](/assets/catprez-sparql.png)
</figure>

## What makes it special?

### Flexible data model

CatPrez uses a [Knowlege Graph](https://en.wikipedia.org/wiki/Knowledge_graph) to store its information. This means it can store anything you can define, so if you want special metadata not normally captured, you can!

The base data model CatPrez uses is [DCAT](https://www.w3.org/TR/vocab-dcat/) which contains basic cataloging properties like:

* title
* created data
* indications of who has a relationship to the resource, like creator, publisher
* relationships to other resources

and so on. CatPrez can have any extension to this you like. Perhaps, in your catalogue of pets, you want to record a cuteness score alongside pet name, no problem: just define what you mean by "pet score" and you can.

### Flexible display

The display of catalogued resources information will automatically reveal common and special properties you record, using a default display logic. So whatever you put in will come back out again.

Here is CatPrez displaying common geometry and custom additional type properties for a resource:

<figure markdown>
![](/assets/catprez-properties.png)
</figure>

You can extend on this with customisable widgets, for example, for scores/metrics for resources. Here is CatPrez showing a [FAIR score](https://data.org/resources/the-fair-data-principles/) for a dataset:

<figure markdown>
![](/assets/catprez-fair.png)
</figure>

### Multiple catalogues

Sometimes it's helpful to have very distinct whole catalogues. CatPrez handles this with... a catalogue of catalogues! You can have any number of distinct collections and resources can appear in one ore more of them.

### Integrations

CatPrez is part of the larger Prez system and shares its data storage with the other parts. This means CatPrez resources can link to vocabularies and spatial data, as well as other resources, and CatPrez can deliver all the parts seamlessly. 

You may want to categorise resources according to one or more vocabularies/controlled term lists and manage those term lists in [VocPrez](vocprez.md).

You may also want to indicate the location of your resources using managed spatial objects in [SpacePrez](spaceprez.md).

## Compared to other catalogue tools

CatPrez _looks_ like common catalogue tools, such as [CKAN](https://ckan.org/) or [GeoNetwork](https://www.geonetwork-opensource.org/) but it's quite different under the hood and thus functions differently. Here are some comparison points:

Aspect | CKAN | GeoNetwork | CatPrez | Notes
--- | --- | --- | --- | ---
**Data Model** | CKAN version of DCAT | ISO19115 or others you define | DCAT-based, extensible model | CKAN uses its own, DCAT-like, model and can be made to deliver other standard models, like ISO19115 _with a lot of effort_! Usually this involves exporting to other applications. GeoNetwork can only really deliver XML data according to ISO19115 schema or others you define in XSLT/schematron files - hard to do. CatPrez can map to any data model you wish to collect data for, with DCAT as a starting point, and can export a wide array of formats like RDF, JSON or XML. You can also pretty easily create new export formats: perhaps you need simple CSV?
**Data Storage** | Postgres database, accessed via an object-relational mapping | XML document DB | Knowledge Graph | CatPrez' DB is more flexible than CKAN's but far more performant and maintainable than GeoNetwork's. The former needs new schema additions for new metadata, the latter needs special indexing across documents (defined schemas) to make properties available 
**UI** | Python API with python templating | Java API & templating | Separate Python API & Vue.js UI | CatPrez uses a newer API system than CKAN and completely separates concerns. This allows UI designers to work on UI without needing to know much about the back-end API
**Tech Stack** | Python - multiple, older, Python API tools (Pyramid, Flask), PostgresDB | Java, relational DB (Postgres, Oracle etc.) | Python (FastAPI newer API tool), RDF Knowledge Graph DB (any one of many) | CatPrez's stack is similar to CKAN's but the application code is mode modern.


## How does it work under the hood?

CatPrez uses a [Knowlege Graph](https://en.wikipedia.org/wiki/Knowledge_graph) created with [RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework) to store all of its content _and_ its configuration. This means that, while it has an expected minimum data model for catalogued items, it can grow when extended information is added with little effort.

Since its configuration data is also stored in the same database, you have full control over how it delivers that data to users and can alter almost anything, just by changing data, not writing software.

CatPrez data can be exported in standardised RDF form and all of it can also be queried via a [SPARQL](https://www.w3.org/TR/sparql11-query/) API. The User Interface itself uses the SPARQL API, so there are no hidden details needed for access and presentation of data. 