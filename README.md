# GS1 Vocabulary RDFLib Namespace Implementation

Welcome to the GS1 Vocabulary RDFLib Namespace Implementation library! This library provides a convenient way to work
with the GS1 Web Vocabulary using RDFLib, a powerful library for working with RDF in Python.

## Features

- **Easy Integration**: Seamlessly integrate the GS1 Vocabulary into your RDFLib projects.
- **Comprehensive Coverage**: Access all terms defined in the GS1 Web Vocabulary.
- **Developer-Friendly**: Simplifies working with GS1 terms in your RDF graphs.

## Installation

Install the library via pip:

```bash
pip install rdflib-gs1
```

## Usage

Here's a quick example of how to use the GS1 Vocabulary with RDFLib:
python

```python
import rdflib
from rdflib_gs1.namespace import GS1

# Create a graph
g = rdflib.Graph()

# Create RDF nodes using the GS1 namespace
product = rdflib.URIRef(GS1.Product)
productID = rdflib.URIRef(GS1.productID)
productName = rdflib.Literal("Example Product")

# Add triples to the graph
g.add((product, rdflib.RDF.type, GS1.Product))
g.add((product, productID, rdflib.Literal("1234567890123")))
g.add((product, GS1.productName, productName))

# Serialize the graph to RDF/XML
print(g.serialize(format='xml').decode('utf-8'))
```

## Contributing

We welcome contributions from the community! Please read our Contributing Guide for guidelines on how to contribute.
License

This project is licensed under the MIT License. See the LICENSE file for details.
About WordLift

WordLift is passionate about contributing to open source projects and enhancing the accessibility and usability of
semantic web technologies. As a proud GS1 partner, WordLift is committed to providing high-quality tools and libraries
to the community.

Thank you for using the GS1 Vocabulary RDFLib Namespace Implementation library! If you have any questions or feedback,
please feel free to open an issue or reach out to us.
