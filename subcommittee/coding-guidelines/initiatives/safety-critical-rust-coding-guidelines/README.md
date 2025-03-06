# Safety-Critical Rust Coding Guidelines

_Note_: Early, subject to changes.

## Building the coding guidelines

SCR uses `Sphinx` to build a rendered version of the coding guidelines, and `uv`_ to install and manage
Python dependencies (including Sphinx itself). To simplify building the rendered version, we created
a script called `make.py` that takes care of invoking Sphinx with the right flags.

You can build the rendered version by running:

```shell
   ./make.py
```

By default, Sphinx uses incremental rebuilds to generate the content that
changed since the last invocation. If you notice a problem with incremental
rebuilds, you can pass the `-c` flag to clear the existing artifacts before
building:

```shell
   ./make.py -c
```

The rendered version will be available in `build/html/`.

A machine-parseable artifact will be available at `build/html/needs.json`.
