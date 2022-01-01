import pytest
import json
import os
import platform


## TODO:  Add support for unix
os_name = platform.system()
curr_path = os.path.dirname(__file__)
standard_lib_path = os.path.abspath("..\\messysoup\\messysoup\\pyodide\\standard_library.json")



def test_standard_lib():

    f = open(standard_lib_path)
    data = json.loads(f.read())
    f.close()

    errors = False

    skip_imports = []

    ## Remove platform specific imports to avoid import errors
    if os_name == "Linux":
        for key, value in data["platform_specific"]["windows"].items():
            skip_imports.append(key)
    else:
        for key, value in data["platform_specific"]["unix"].items():
            skip_imports.append(key)

    for key, value in data["standard_lib"].items():
        if value["supported"] == True and key not in skip_imports:
            try:
                __import__(key)
            except ImportError:
                errors = True
                print(f"Unable to import {key}")

    assert errors == False