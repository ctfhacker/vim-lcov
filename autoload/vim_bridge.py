#!/usr/bin/env python3

import vim
import os

import lcov_parser


def vim_lcov_highlight_uncovered_lines(lcov_filepath):
    eof_line_number = int(vim.eval("line('$')"))

    if not os.path.isfile(lcov_filepath):
        log = "[vim-lcov][ERROR]: no such file {}".format(lcov_filepath)
        vim.command('echohl ErrorMsg | echo "' + log + '" | echohl None')
        return False

    # NOTE: sign id must be number > 0 and uniq in some group
    sign_id_start = 1
    group = 'vim-lcov_' + vim.current.buffer.name

    # remove all previous signs if exist
    vim.command(
        'exe ":sign unplace * group=' +
        group +
        ' file=".expand("%:p")')

    priority = 9999  # NOTE: default value is 10
    for sign_id, (line_number, count) in enumerate(
        lcov_parser.uncovered_line_numbers_generator(
            lcov_filepath, os.path.basename(vim.current.buffer.name)), start=sign_id_start):

        if count == 0:
            name = 'vim_lcov_uncovered'
        else:
            name = 'vim_lcov_covered'

        vim.command(
            'exe ":sign place ' +
            str(sign_id) +
            ' line=' +
            str(line_number) +
            ' group=' + group +
            ' priority=' + str(priority) +
            ' name=' + str(name) + ' file=".expand("%:p")')

    return True
