Thue-Morse Paper Draft
======================

In this repo, I keep all notes and files related to my research on extending the Thue-Morse sequence to n-ary rigorously. It is structured as:

Repository Structure
--------------------

.. code-block:: text

   /
   ├── LICENSE                  # License file
   ├── README.rst               # Project readme
   ├── update_overleaf_repo.sh  # Bash script to update the repository from Overleaf tar and PDF
   ├── rendered.pdf             # Compiled PDF output of the Overleaf project
   └── src/                     # Directory containing the LaTeX source files
       ├── main.tex             # Main LaTeX file (the entry point for compiling)
       ├── references.bib       # Bibliography file (uses BibTeX for citations)
       ├── figures/             # Directory for image files used
       └── other.tex            # Additional LaTeX files for appendices, etc.

Usage
-----

To run the script, provide the zip file and the PDF file as arguments:

.. code-block:: bash

    ./update_overleaf_repo.sh project.zip output.pdf "Updated Overleaf project"
