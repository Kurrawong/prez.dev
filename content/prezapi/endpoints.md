---
title: API Endpoints
#description: The API for Prez
---

## Endpoints

Prez delivers the following endpoints:

### Core Endpoints

**Endpoint** | **Default MT**
--- | ---
/ | text/anot+turtle
/docs | text/html
/catalogs/{catalogId} | text/anot+turtle
/catalogs/{catalogId}/collections | text/anot+turtle
/catalogs/{catalogId}/collections/{recordsCollectionId} | text/anot+turtle
/catalogs/{catalogId}/collections/{recordsCollectionId}/items | text/anot+turtle
/catalogs/{catalogId}/collections/{recordsCollectionId}/items/{itemId} | text/anot+turtle
/purge-tbox-cache | application/json
/tbox-cache | application/json
/health | application/json
/prefixes | text/anot+turtle
/concept-hierarchy/{parent_curie}/narrowers | text/anot+turtle
/concept-hierarchy/{parent_curie}/top-concepts | text/anot+turtle
/cql | text/anot+turtle
/profiles | text/anot+turtle
/search | text/anot+turtle
/profiles/{profile_curie} | text/anot+turtle
/object | text/anot+turtle
/identifier/redirect | N/A
/identifier/curie/{iri} | text/plain
/identifier/iri/{curie} | text/plai

### OGC Features API Endpoints

**The OGC Features API Endpoints are based at the ROOT `/catalogs/{catalogId}/collections/{recordsCollectionId}/`**

**Endpoint** | **Default MT**
--- | ---
{ROOT}/features | application/json
{ROOT}/features/docs | text/html
{ROOT}/features/conformance | application/json
{ROOT}/features/collections | application/json
{ROOT}/features/collections/{collectionId} | application/json
{ROOT}/features/collections/{collectionId}/items | application/geo+json
{ROOT}/features/collections/{collectionId}/items/{featureId} | application/geo+jso

