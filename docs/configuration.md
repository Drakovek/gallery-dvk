# Configuration

Configuration files for *gallery-dvk* are stored in JSON format.
A default config file can be found at [gallery-dvk.json](./gallery-dvk.json)
A more in-depth example config file can be found at [gallery-dvk-example.json](./gallery-dvk-example.json)

## Extractor Options

If you're used to [gallery-dl](https://github.com/mikf/gallery-dl), the configuration structure here is simplified considerably. Instead of separate keys for extractors, post-processors, etc., there are only extractors and their options in *gallery-dvk*.

Each extractor is identified by a `category`, which is simply the site name for the extractor in all lowercase without special characters or spaces. For example, the `category` for [https://www.transfur.com](https://www.transfur.com) is `transfur`.

All options are simply keys within that category. Again, you can look at [gallery-dvk.json](./gallery-dvk.json) or [gallery-dvk-example.json](./gallery-dvk-example.json) for some examples of how this works.

### \*.metadata

***Type***
+ `bool`

***Default***
+ `false`

***Descripton***

Whether to write a JSON file containing metadata for each media file downloaded by the extractor.

### \*.filename_format

***Type***
+ `string`

***Default***
+ `"{id}_{name}"`

***Description***

The format to use for naming files downloaded using this extractor. Strings between curly braces are treated as keys, and will be replaced with the corresponding value of that key in the metadata of the URL being downloaded. You can use any keythat can be seen in the downloaded JSON metadata you get when the `metadata` option is set to `true` in the extractor.

All extractors will have {title} and {id} keys available to use, and most extractors will have {artist} and {date} keys to use as well. All strings not in curly brackets will be used as-is.

### \*.archive

***Type***
+ `string`

***Default***
+ `null`

***Example***

    "archive": "/path/to/archive/extractor-archive.db"

***Description***

Path to an archive file that will store IDs for all the URLs downloaded by this extractor. When set, the extractor will add an ID to the archive for each URL that is downloaded, and will not download a URL if a corresponding ID already exists in the archive. This allows the extractor to skip over any given URLs that have already been downloaded, and only spend time downloading new URLs.

If the given archive file does not exist, the extractor will create the archive the first time it is run, given that the parent directory for the archive file is valid.

If the archive is set to `null`, this extractor will not create an archive, and it will not keep track of which URLs have already been downloaded.

### \*.username & password

***Type***
+ `string`

***Default***
+ `null`

***Example***

    website:
    {
        "username": "USERNAME",
        "password": "PASSWORD"
    }

***Description***

The login credentials for the extractor. This is required to access locked content for `transfur`.

If set to `null`, *gallery-dvk* will prompt the user for username and password if necessary.

### \*.webpage_sleep & download_sleep

***Type***
+ `number`

***Default***
+ `1.5`

***Example***

    website:
    {
        "webpage_sleep": 1.0,
        "download_sleep": 2.5
    }

***Description***

The amount of time to wait in seconds after loading a webpage and downloading a file, respectively. Increasing this wait time can reduce load on bandwidth and reduce the number of response errors.

## Extractor-Specific Options

### transfur.include

***Type***
+ `list` of `strings`

***Default***
+ `["gallery", "sketches"]`

***Descrtiption***

A list of subcategories to include when processing a user profile.

Possible values are `"gallery"`, `"sketches"`, and `"favorites"`

### docslab.include

***Type***
+ `list` of `strings`

***Default***
+ `["submissions"]`

***Descrtiption***

A list of subcategories to include when processing a user profile.

Possible values are `"submissions"` and `"favorites"`

### docslab.download_artwork

***Type***
+ `bool`

***Default***
+ `false`

***Descripton***

Whether to automatically download associated artwork submissions when downloading story submissions.

### docslab.download_stories

***Type***
+ `bool`

***Default***
+ `false`

***Descripton***

Whether to automatically download parent story submissions when downloading artwork submissions.
