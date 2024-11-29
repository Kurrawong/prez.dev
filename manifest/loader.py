"""
This script creates an n-quads files containing the following by parsing a Prez Manifest:

 1. A Named Graph for each content item using the item's IRI as the graph IRI
 2. A Named Graph for the container either using the container's IRI as the graph IRI if given, or by making one up if a Blank Node
 3. All the triples in resources with roles mrr:completeContainerAndContentLabels & mrr:incompleteContainerAndContentLabels within a Named Graph with IRI <https://background>
 4. An Olis Virtual Graph, <https://olis.dev/VirtualGraph> object which is as an alias for all the Named Graphs from 1., 2. & 3.
 5. Entries in the System Graph - Named Graph with IRI <https://olis.dev/SystemGraph> - for each Real and the Virtual Graph

Run this script with the -h flag for more help, i.e. ~$ python documentor.py -h
"""

