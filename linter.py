#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Olivier Colot
# Copyright (c) 2017 Olivier Colot
#
# License: MIT
#

"""This module exports the Credo plugin class."""

from SublimeLinter.lint import Linter, util


class Credo(Linter):
    """Provides an interface to credo."""

    cmd = 'mix credo --format=flycheck @'
    regex = (
        r'^.+?:(?P<line>\d+):((?P<col>\d+):)? '
        r'(?:(?P<error>[W])|(?P<warning>[R|F|C])): '
        r'(?P<message>.+)$'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    word_re = None
    defaults = {
        'selector': 'source.ex - meta.attribute-with-value, source.exs, source.eex'
    }
