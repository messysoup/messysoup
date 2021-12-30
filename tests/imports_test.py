import pytest
import json
import os
import platform

os_name = platform.system()
curr_path = os.path.dirname(__file__)
standard_lib_path = os.path.abspath("..\\messysoup\\messysoup\\pyodide\\standard_library.json")



def test_standard_lib():

    f = open(standard_lib_path)
    data = json.loads(f.read())
    f.close()

    errors = False

    ## Remove platform specific imports to avoid import errors
    if os_name == "Linux":
        for i in data["platform_specific"]["windows"]:
            data["standard_lib"].remove(i)
    else:
        for i in data["platform_specific"]["unix"]:
            data["standard_lib"].remove(i)

    for i in data["standard_lib"]:
        try:
            __import__(i)
        except ImportError:
            errors = True
            print(f"Unable to import {i}")

    assert errors == False