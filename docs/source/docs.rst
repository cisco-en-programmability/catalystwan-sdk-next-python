================================================
How to generate documentation
================================================

This guide provides instructions on how to generate Sphinx documentation for the CatalystWAN Python project.

Installation of Required Libraries
==================================

Before generating the documentation, ensure that you have Sphinx and its dependencies installed in your environment. You can do this by running the following command:

.. code-block:: bash

   pip install sphinx sphinx-rtd-theme myst-parser sphinx-design

- **sphinx**: The core Sphinx package for generating documentation.
- **sphinx-rtd-theme**: A popular theme for Sphinx documentation (optional).
- **sphinx-design**: Extension for interactive components (optional).

Building the Documentation
==========================

Once everything is set up, you can generate the HTML documentation by running:

.. code-block:: bash

   cd docs
   make html

This command will build the documentation and place the output in the `docs/build/html` directory. You can open `index.html` in a web browser to view the generated documentation.

Conclusion
==========

By following these steps, you can efficiently generate and manage documentation for the CatalystWAN Python project using Sphinx. Make sure to explore Sphinx's extensive capabilities to enhance and customize your documentation further.
