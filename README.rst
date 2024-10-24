Thue-Morse Paper Draft
======================

In this repo, I keep all notes and files related to my research on extending the Thue-Morse sequence to n-ary
rigorously. It is structured as:

Repository Structure
--------------------

.. code-block:: text

  /
  ├── LICENSE                        # License file
  ├── README.rst                     # Project readme
  ├── update_from_overleaf.{bat,sh}  # Scripts to update the repository from Overleaf ZIP and PDF
  ├── rendered.pdf                   # Compiled PDF output of the Overleaf project
  ├── src/                           # Directory containing the LaTeX source files
  │   ├── main.tex                   # Main LaTeX file (the entry point for compiling)
  │   ├── macros.tex                 # LaTeX file that contains utility functions
  │   ├── references.bib             # Bibliography file (uses BibTeX for citations)
  │   └── figures/                   # Directory for image files used
  └── code/                          # Directory with associated code
      ├── README.rst                 # Readme for associated code
      ├── __init__.py                # Empty file that allows this folder to be used as a module
      ├── args.py                    # A utility file that deals with command line argument parsing
      ├── test_seq.py                # A test file that allows you to check sequence equality
      └── p{2,n}_[1-9]d.py           # The file for def. [1-9] of the Thue-Morse Seq. for {2,n} players

Usage
-----

To run the update script, provide the zip file and the PDF file as arguments:

.. code-block:: bash

  ./update_overleaf_repo.sh project.zip output.pdf ["commit message"]

In a Windows environment, it runs similarly, though you need to use the batch file version:

.. code-block:: bat

  ./update_overleaf_repo.bat project.zip output.pdf ["commit message"]

Square brackets indicate an optional argument. If a commit message is not provided, git will prompt you for one.
