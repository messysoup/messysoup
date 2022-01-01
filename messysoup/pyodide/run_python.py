import inspect
import json
import os
import platform
from pathlib import Path


script_location = ""

def get_supported_imports():
    ## TODO:  Add support for unix
    os_name = platform.system()
    curr_path = os.path.dirname(__file__)
    supported_lib_path = os.path.abspath(f"{curr_path}\\supported_imports.json")
    standard_lib_path = os.path.abspath(f"{curr_path}\\standard_library.json")


    f = open(standard_lib_path)
    standard_lib = json.loads(f.read())
    f.close()

    f = open(supported_lib_path)
    supported_lib = json.loads(f.read())
    f.close()

    return standard_lib, supported_lib

def all_supported_packages(standard_lib: list, supported_lib: dict):
    all_supported_packages = []

    for key, value in standard_lib["standard_lib"].items():
        if value["supported"] == True:
            all_supported_packages.append(key)

    for key, value in supported_lib['packages'].items():
        all_supported_packages.append(value['import_name'])

    return all_supported_packages


def get_script_contents():

    with open(script_location) as f:
        py_script = f.readlines()

    # Removes required imports and function call.
    # Might need to make this more robust so as to not
    # remove comments, variables, etc. containing `run_python`.
    for i in py_script:
        if "run_python" in i or "messysoup.pyodide" in i:
            py_script.remove(i)

    print(py_script)

    return py_script


def get_imports():
    '''
    Gets all the imported packages from a file.
    Returns a nested list of packages imported that are supported,
    and those that are not supported.
    '''

    imported_packages = []
    non_supported_packages = []

    standard_lib, supported_lib = get_supported_imports()
    available_packages = all_supported_packages(standard_lib, supported_lib)

    ## Fetches the imported packages and compares them against the list
    ## of supported packages.  Add supported imported packages to the list,
    ## and raise an `ImportError` if they are not.
    for line in get_script_contents():

        # Discard all other lines of code
        if line.startswith("import") or line.startswith("from"):
            line = line.split()
            attempted_import = line[1]

            # To handle relative imports
            if ".." in attempted_import:
                non_supported_packages.append(attempted_import)

            # Checks if importing submodule from package.
            # Only looks at top level package name
            elif "." in attempted_import:
                import_split = attempted_import.split(".")
                attempted_import = import_split[0]

                if attempted_import in available_packages:
                    imported_packages.append(attempted_import)
                else:
                    non_supported_packages.append(attempted_import)

            # Handle basic import 
            elif attempted_import in available_packages:
                    imported_packages.append(attempted_import)
            
            else:
                non_supported_packages.append(attempted_import)
        else:
            pass
    
    if len(non_supported_packages) > 0:
        raise ImportWarning(f'{", ".join(non_supported_packages)} are not supported.  If you are sure they are installed and supported, make sure to add them to `supported_imports.json`.')

    return [imported_packages, non_supported_packages]

#TODO: Add micropip to load and import the imports from `get_imports()`
def setup():
    setup = f"""
async function main(){{
    let pyodide = await loadPyodide({{
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/"
    }});
    pyodide.loadPackage(
        {get_imports()[0]}
    )
    pyodide.runPython(`
{"".join(get_script_contents())}
    `)
}}
main()
    """
    return setup

def run_python(file_name: str, dir_: str=script_location):
    '''
    The defualt file location will be the same location as the file
    this function is called from.  Make sure to include the `.js` suffix
    with the filename.
    A helper function will remove any line with ` run_python(`.  Make sure
    to not include this in any other function, method, comment, or 
    docstring.
    This will overwrite any content previously in the output.
    '''
    global script_location 
    script_location = inspect.stack()[1].filename

    root = ""

    if dir_ == "":
        root = Path(script_location).parent.absolute()
    else:
        root = dir_

    f = open(f"{root}\\{file_name}", 'w')
    f.write(setup())
    f.close


    