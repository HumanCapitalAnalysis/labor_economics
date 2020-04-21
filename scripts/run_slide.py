#!/usr/bin/env python
"""This module compiles the lecture notes."""
import subprocess
import shutil
import os

from auxiliary import parse_arguments
from auxiliary import LECTURES_ROOT


def compile_single(is_update):
    """Compile a single lecture."""
    for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
        subprocess.check_call(task + ' main', shell=True)
    shutil.move("main.pdf", "slides.pdf")


if __name__ == '__main__':

    request = parse_arguments('Create lecture slides')


    os.chdir(LECTURES_ROOT)

    for dirname in request:
        os.chdir(dirname)
        compile_single('slides')
        os.chdir('../')