#!/usr/bin/python
import os
def generator(path, extension):
    for file in os.listdir(path):
        if file.split(".")[-1] == extension:
            yield file

for file in generator('C:/', 'zip'):
    print file