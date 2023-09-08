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

A specalised [OGC Rescords API](https://ogcapi.ogc.org/records/) technical interface:

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


## How does it work under the hood?