from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class PREZ(DefinedNamespace):

    _NS = Namespace("https://prez.dev/")
    _fail = True

    Manifest: URIRef
