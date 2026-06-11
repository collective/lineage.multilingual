<div align="center">
    <h1 align="center">lineage.multilingual</h1>
</div>
<div align="center">
[![PyPI](https://img.shields.io/pypi/v/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)
[![PyPI - License](https://img.shields.io/pypi/l/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)
[![PyPI - Status](https://img.shields.io/pypi/status/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/lineage.multilingual)](https://pypi.org/project/lineage.multilingual/)

[![CI](https://github.com/collective/lineage.multilingual/actions/workflows/main.yml/badge.svg)](https://github.com/collective/lineage.multilingual/actions/workflows/main.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/collective/lineage.multilingual)](https://github.com/collective/lineage.multilingual)
[![GitHub Repo stars](https://img.shields.io/github/stars/collective/lineage.multilingual?style=social)](https://github.com/collective/lineage.multilingual)

</div>

Multilingual configuration for lineage child sites

## Features

With this package, if you set a custom set of languages in a Lineage ChildSite, the `LRF`s that correspond to the selected languages will be created inside the ChildSite.

This is useful when you want to have a different set of languages in the root of the site and in the child site.

It also helps to have the language URLs inside the childsite.

And how we do it?

We just override the [subscriber](https://github.com/plone/plone.app.multilingual/blob/master/src/plone/app/multilingual/subscriber.py#L184) that plone.app.multilingual has to create the `LRF`s in the root of the site, and call it with the context where the language settings are being applied.

If using this with [collective.lineage](https://github.com/collective/collective.lineage) you may want to install also [lineage.registry](https://github.com/collective/lineage.registry) for having a local registry in child sites, and [lineage.controlpanels](https://github.com/collective/lineage.controlpanels) to be able to set local values for the registry in the childsite.

Until a new release of plone.app.multilingual is ready, this package needs [this branch](https://github.com/plone/plone.app.multilingual/tree/erral-aqbase-setupsite) of plone.app.multilingual.

## Installation

Install lineage.multilingual with `pip`:

```shell
pip install lineage.multilingual
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/collective/lineage.multilingual/issues)
- [Source code](https://github.com/collective/lineage.multilingual/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/lineage.multilingual.git
    cd lineage.multilingual
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Add features using `plonecli` or `bobtemplates.plone`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

You can add a behavior with the following command.

```shell
make add behavior
```

```{seealso}
You can check the list of available subtemplates in the [`bobtemplates.plone` `README.md` file](https://github.com/plone/bobtemplates.plone/?tab=readme-ov-file#provided-subtemplates).
See also the documentation of [Mockup and Patternslib](https://6.docs.plone.org/classic-ui/mockup.html) for how to build the UI toolkit for Classic UI.
```

## License

The project is licensed under GPLv2.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (2.0.0a3)](https://github.com/plone/cookieplone) and [cookieplone-templates (6678734)](https://github.com/plone/cookieplone-templates/commit/6678734cc3713f3fab9ea510616cef59dc466514) on 2026-06-11 10:38:21.066582. A special thanks to all contributors and supporters!
