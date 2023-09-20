#!/usr/bin/env python3

"""Setuptools setup file."""

import setuptools

console_scripts = ["gallery-dvk = gallery_dvk.gallery_dvk:main"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gallery-dvk",
    version="0.1.7",
    author="Drakovek",
    author_email="DrakovekMail@gmail.com",
    description="Utility for downloading media from various image hosting websites.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drakovek/gallery-dvk",
    packages=setuptools.find_packages(),
    install_requires=["beautifulsoup4",
                "HTML-String-Tools",
                "Metadata-Magic",
                "Pillow",
                "Python-Print-Tools",
                "requests",
                "tqdm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.0',
    entry_points={"console_scripts": console_scripts}
)
