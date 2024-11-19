Code
====

In this directory, you can find my implementations of each definition of the Thue-Morse Sequence and its extensions. To
run any given definition, call:

.. code-block::

  python -m dev.p{2,n}.d[0-9][0-9] <items to generate> [<number of players, if n players>]

The 2 player definitions only support base 2

The n player definitions support:
- positive integer bases >1 (all)
- negative integer bases <-1
  - d01
  - d02
  - d06 (but currently produces incorrect answers)
  - d07 (but currently produces incorrect answers)
