from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef

class MRR(DefinedNamespace):

    _NS = Namespace("http://www.w3.org/ns/org#")
    _fail = True

    ContainerData: URIRef
    ContainerModel: URIRef
    ContentData: URIRef
    ContentModel: URIRef
    ContainerAndContentModel: URIRef
    CompleteContainerAndContentLabels: URIRef
    IncompleteContainerAndContentLabels: URIRef
