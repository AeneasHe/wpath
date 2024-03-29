# coding=utf-8

from setuptools import setup, find_namespace_packages

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

NAME = "wpath"

DESCRIPTION = "package help find the project root folder."

KEYWORDS = "project root folder workspace"

AUTHOR = "Aeneas"

AUTHOR_EMAIL = "aeneas.he@gmail.com"

URL = "https://github.com/aeneashe/wpath"

VERSION = "0.1.4"

LICENSE = "MIT"

setup(
    name=NAME,
    version=VERSION,
    python_requires=">=3.7",
    install_requires=["print_pretty", "colorama"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=LICENSE,
    packages=find_namespace_packages(),
    include_package_data=True,
    zip_safe=True,
)
