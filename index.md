# FANCY-CLI
<img alt="fancy logo" src="images/fancy-logo.png" width=64>

<link rel="shortcut icon" type="image/x-icon" href="images/fancy-logo.png">

FANCY is a command-line interface (CLI) tool written in Python that creates fancy-looking folder icons like

<img alt="fancy example" src="images/example.png" width=90>
<span style="font-size: 0.3rem">Python icon by (Babolix)[https://macosicons.com/#/u/babolix] on [MacOSIcons](https://macosicons.com/#/). Original Python logo made by <https://www.python.org/>.</span>

with ease!

## Installation

Install using python pip:

```bash
pip install fancy-cli

# OR if that doesn't work, try

python3 -m pip install fancy-cli
```

### Troubleshooting

If both of the two commands above don't work, then try creating a virtual environment to house your packages. In short, a virtual environment contains Python packages without them having to be installed system wide. To create one, run `python3 -m venv .venv` in your terminal, creating a folder `.venv` in your current working directory. Now, activate it with `source .venv/bin/activate`. If you use a shell with a different syntax than bash, like `fish`, use the shell-appropriate version of the `activate` file instead. For `fish` users, do `source .venv/bin/activate.fish`. Now you should be able to `pip install fancy-cli`.

If that doesn't work, maybe you haven't [downloaded Python](https://www.python.org/downloads/).
If you have Python installed, you might not have `pip` installed for some reason, although usually `pip` is bundled with Python. [This page](https://pip.pypa.io/en/stable/installation/) explains how to get `pip`. Once you have gotten both of those installed, you might also need to create and activate a virtual environment, explained in the previous paragraph, but once you activate the virtual environnment, you should be good to go!

## Usage

To view all available features, run:

```bash
fancy --help
```

in your terminal.

As an example, to turn the icon at `~/Downloads/HTML-icon.png` into a red folder located at `~/Downloads/HTML-folder.png` using FANCY-CLI, run:

```bash
fancy ~/Downloads/HTML-icon.png ~/Downloads/HTML-folder.png --color "red"
```

## Related webpages

Documentation at <https://fancy-projects.github.io>

PyPI page at <https://pypi.org/project/fancy-cli/>

GitHub page at <https://github.com/fancy-projects/fancy-cli/>

FAQ
Changelog