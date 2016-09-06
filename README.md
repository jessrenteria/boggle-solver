# Boggler
A Boggle word finder written in Python 3.
It works with rectangular boards of arbitrary dimensions.
The output is sorted by order of decreasing length.

Usage:

    python boggler.py grid_file dict_file found_file

- `grid_file`: file with space separated characters representing the board
- `dict_file`: file of newline separated valid words
- `found_file`: file to write found words

Benchmarks:
- Forms prefix tree of around 200,000 words and finds all words in a 4x4 grid in under 3 seconds on a 2013 MacBook Pro
