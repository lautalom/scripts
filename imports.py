import glob
import os
import ast
from collections import namedtuple
import re

def get_imports(path):
    Import = namedtuple("Import", ["module", "name", "alias"])
    with open(path) as fh:
        root = ast.parse(fh.read(), path)
    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):
            module = node.module.split('.')
        else:
            continue
        for n in node.names:
            yield Import(module, n.name.split('.'), n.asname)

def sep(a):
    if a == 1:
        print(end='----------------------------------------------------------------\n')
    else:
        print(end='================================================================\n')

def list_methods(imp, path):
    text = open(path, 'r')
    filetext = text.read()
    text.close()
    exp = imp
    matches = re.findall(rf'{exp}\.[^\(\:\)\ \n]*', filetext)
    print(set(matches))
    sep(1)

def run(path):
    os.chdir(path)
    extensions = [".cpp", ".py"]
    f = "*"+extensions[1]
    for file in glob.glob(f):
        sep(2)
        print("FILENAME: " + file)
        a = get_imports(file)
        for imp in a:
            print(
                imp)
            if imp[2]:
                list_methods(imp[2], path+'/'+file)
            else:
                list_methods(imp[1][0], path+'/'+file)

if __name__ == '__main__':
    path = os.getcwd()
    ch = input("Run in " + path + "?\t [Y]/N\n")
    while ch and (ch.lower()[0] == 'n' or ch.lower()[0] != 'y'):
        path = input("Input correct absolute path: \n")
        if not os.path.exists(path):
            print("Path does not exist or is not a directory, Try again")
            user = input(f"{path} is correct? \tDefault: [N]/Y\n")
            if not user or user.lower()[0] == 'y' or not user:
                print("Path not found. Terminating.")
                exit(0)
        else:               
            ch = "y"
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d[0] == '.']
        sep(3)
        print("Directory: " + root)
        run(root)
        sep(3)
