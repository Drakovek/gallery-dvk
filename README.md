# gallery-dvk

*gallery-dvk* is a command-line program designed to download media from various media sharing websites: [See Supported Sites](./docs/supportedsites.md)

It is heavily inspired by [gallery-dl](https://github.com/mikf/gallery-dl), and if I were smart, I probably would have just forked gallery-dl, but I couldn't fully wrap my head around how the codebase works, so here we are. I may not be able to parse the code very well, but I've ripped off gallery-dl's user documentation pretty thoroughly here.

Contents:
+ [Installation](#installation)
+ [Usage](#usage)
+ [Configuration](#configuration)
+ [Authentication](#authentication)

## Installation

*gallery-dvk* can be downloaded from it's PyPI package using pip:

    pip3 install gallery-dvk

If you are installing from source, the following python packages are required:
+ [beautifulsoup4](https://code.launchpad.net/beautifulsoup)
+ [HTML-String-Tools](https://github.com/Drakovek/HTML-String-Tools)
+ [Metadata-Magic](https://github.com/Drakovek/MetadataMagic)
+ [Python-Print-Tools](https://github.com/Drakovek/Python-Print-Tools)
+ [requests](https://requests.readthedocs.io/en/latest)
+ [tqdm](https://pypi.org/project/tqdm)
+ [pillow](https://github.com/python-pillow/Pillow) \(If using image stitching for Webtoon\)

## Usage

To use *gallery-dvk* call it with the URL you wish to download from:

    gallery-dvk URL

You can also download a from a list of URLs from a text file:

    gallery-dvk -i FILE

Use `gallery-dvk --help` for a full list of command-line options. You can access aditional options and configuration using a config file.

## Configuration

Configuration files for *gallery-dvk* are stored in JSON format.

### Documentation

Documentation for all the available configuration options can be found at [/docs/configuration.md](./docs/configuration.md)

A default config file can be found at [/docs/gallery-dvk.json](./docs/gallery-dvk.json)
A more in-depth example config file can be found at [/docs/gallery-dvk-example.json](./docs/gallery-dvk-example.json)

### Location

*gallery-dvk* looks for config files in the following locations:

**WINDOWS:**
+ `%APPDATA%\gallery-dvk\config.json`
+ `%USERPROFILE%\gallery-dvk\config.json`
+ `%USERPROFILE%\gallery-dvk.json`

(`%USERPROFILE%` usually refers to a user's home directory, i.e. C:\Users\<username>\)

**LINUX/MAC/UNIX-BASED:**
+ `/etc/gallery-dvk.json`
+ `${HOME}/.config/gallery-dvk/config.json`
+ `${HOME}/.gallery-dvk.json`

## Authentication

### Username and Password

Most extractors require login credentials to access some locked content, and some require login credentials to access the site at all.

You can set the necessary login information in your [configuration file](#configuration).

    {
        "transfur":
        {
            "username": "<USERNAME>",
            "password": "<PASSWORD>"
        }
    }