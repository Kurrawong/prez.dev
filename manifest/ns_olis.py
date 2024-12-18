from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef


class OLIS(DefinedNamespace):

    _NS = Namespace("https://olis.dev/")
    _fail = True

    NamedGraph: URIRef
    RealGraph: URIRef
    SystemGraph: URIRef
    VirtualGraph: URIRef

    isAliasFor: URIRef
