"""
Part2 directory & file analyzer module
Hanrun Li
"""

import collections
from os import listdir
from os import chdir
# from prettytable import PrettyTable
import prettytable


def analyze(directory):
    """ function to analyze the dir """
    try:
        listdir(directory)
    except OSError:
        return
    else:
        pass

    flist = listdir(directory)
    chdir(directory)
    result = {}
    ptable = prettytable.PrettyTable()
    ptable.field_names = ["File Name", "Classes", "Functions", "Lines", "Characters"]

    for file_name in flist:
        # only deal with .py files
        if file_name.endswith('.py'):
            try:
                fprocess = open(file_name, 'r')
            except FileNotFoundError:
                print("Can't open", file_name)
            else:
                with fprocess:
                    subdic = collections.defaultdict(int)
                    if directory.endswith('/'):
                        subdic["filename"] = directory + file_name
                    else:
                        subdic["filename"] = directory + '/' +  file_name
                    for line in fprocess:
                        subdic["chars"] += len(line)
                        subdic["lines"] += 1
                        if line.strip().startswith('def '):
                            subdic["funcs"] += 1
                        if line.strip().startswith('class '):
                            subdic["classes"] += 1
                    ptable.add_row(
                        [subdic["filename"],
                         subdic["classes"],
                         subdic["funcs"],
                         subdic["lines"],
                         subdic["chars"]]
                        )
                    result[file_name] = subdic
    print("\nSummary for " + directory)
    print(ptable)
    return result
