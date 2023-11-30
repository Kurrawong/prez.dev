![](assets/prez-logo.png)

## What is Prez?

Prez is an open source web application that delivers "profiles of Knowledge Graph data".

Prez is used to publish:

* lists of managed vocabularies
* highly configurable catalogues of digital resources
* spatial reference datasets

While being open source, Prez is mostly maintained by [KurrawongAI](https://kurrawong.ai) who provide professional services to assist with its use.

## How can I get Prez?

You can run Prez yourself by understanding how it works (see below) and running all the parts.

Or you can contact [KurrawongAI](https://kurrawong.ai) who can assist you.

## How does Prez work?

Prez is available for use as two components:

* [Prez](https://github.com/rdflib/prez/) - an API that 'slices and dices' Knowledge Graph data source according to data structure definitions
* [Prez UI](https://github.com/RDFLib/prez-ui) - a web user interface that displays data from the Prez API

These components require a Knowledge Graph database to store the data Prez uses.

Additionally, Prez relies on management of processes to load data into a Knowledge Graph database. These can be implemented in many ways, such s workflows within version control systems. 

