import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "readme.md").read_text()

setup(
    name="messysoup",
    version="0.0.3",
    description="A wrapper for html",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/messysoup/messysoup",
    author="messysoup",
    author_email="messysoup@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",    
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    include_package_data=True,
)