#!/usr/bin/env python3

import os

for (root, dirs, files) in os.walk('.', topdown=True):
    print(f"ROOT: {root}")
    if '.git' in dirs:
        print("removing .git")
        dirs.remove('.git')

    # lowercase all files
    print(f"files: {files}")
    for file in files:
        if file.islower():
            print(f"passing: {file}")
            continue
        print(f"renaming: {file} -> {file.lower()}")
        os.rename(os.path.join(root, file), os.path.join(root, file.lower()))

    lowers = list()
    toremove = list()

    # lowercase all dirs
    print(f"dirs: {dirs}")
    for dir in dirs:
        if dir.islower():
            print(f"passing: {dir}")
            continue
        print(f"renaming: {dir} -> {dir.lower()}")
        os.rename(os.path.join(root, dir), os.path.join(root, dir.lower()))
        lowers.append(dir.lower())
        toremove.append(dir)
    
    for rm in toremove:
        print(f"removing {rm}")
        dirs.remove(rm)

    # walk the new dirs
    dirs.extend(lowers)

    print(f"new dirs {dirs}")
