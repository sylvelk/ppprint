#!/usr/bin/env python
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ppprint",
    version="0.1.0",
    author="Sylvain El-Khoury",
    author_email="sylvelk@gmail.com",
    description="An easy to use Python Pretty Print",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sylvelk/ppprint",
    project_urls={
        "Bug Report": "https://github.com/sylvelk/ppprint/issues/new?template=bug_report.md",
        "Feature Request": "https://github.com/sylvelk/ppprint/issues/new?template=feature_request.md",
        "Documentation": "https://github.com/sylvelk/ppprint/tree/master/ppprint",
        "Source Code": "https://github.com/sylvelk/ppprint",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="print pretty console progress bar",
    test_require=['pytest']
)
