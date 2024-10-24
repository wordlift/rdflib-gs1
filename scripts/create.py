import keyword
import os.path
import re
from datetime import datetime

from rdflib import Graph, Namespace
from rdflib.namespace import RDFS
from rdflib.term import URIRef


def sanitize_identifier(name):
    # Replace invalid characters with underscore
    name = re.sub(r"\W|^(?=\d)", "_", name)
    # Append underscore if it's a Python keyword
    if keyword.iskeyword(name):
        name += "_"
    return name


def create():
    # Load the GS1 vocabulary
    g = Graph()
    in_filename = os.path.join(os.path.dirname(__file__), "..", "files/gs1Voc.ttl")
    g.parse(in_filename, format="turtle")

    # Get the GS1 namespace
    GS1 = Namespace("https://ref.gs1.org/voc/")

    # Collect terms and their comments
    terms = {}

    for s in g.subjects():
        if isinstance(s, URIRef) and s.startswith(GS1):
            term_name = s.split(str(GS1))[-1]
            # Skip blank terms
            if not term_name:
                continue
            # Get the comment/documentation
            comment = g.value(s, RDFS.comment)
            # Clean up the comment
            if comment:
                comment = str(comment).replace("\n", " ").strip()
            else:
                comment = ""
            terms[term_name] = comment

    # Prepare the header
    header = '''
from rdflib.namespace import DefinedNamespace, Namespace
from rdflib.term import URIRef

class GS1(DefinedNamespace):
    """
    GS1 vocabulary namespace elements

    Generated from: https://www.gs1.org/voc/data/gs1Voc.ttl
    Date: {date}
    """

    _NS = Namespace("https://ref.gs1.org/voc/")

'''.format(
        date=datetime.now().strftime("%Y-%m-%d")
    )

    # Write to the _GS1.py file
    out_filename = os.path.join(
        os.path.dirname(__file__), "..", "rdflib_gs1/namespace/_GS1.py"
    )
    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(header)
        for term, comment in sorted(terms.items()):
            sanitized_term = sanitize_identifier(term)
            # Write the term as a class attribute
            if comment:
                f.write(f"    {sanitized_term}: URIRef  # {comment}\n")
            else:
                f.write(f"    {sanitized_term}: URIRef\n")


if __name__ == "__main__":
    create()
