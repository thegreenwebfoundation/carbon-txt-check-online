# carbon-txt-check-online

A demo plugin for the carbon.txt validator that checks that files linked in carbon.txt files are still online.


## Installation

Install this plugin in the same environment as the carbon.txt validator.

The validator is listed as dependency, so if you install this package and the validator isn't already installed, you will also download the carbon.txt validator CLI tool as well.

### Using `pip`

Make sure you are in your chosen virtual environment, then run:

```bash
pip install carbon-txt-check-online
```

### Using `uv`

Inside a project with a pyproject.toml file, run the following:

```bash
uv add carbon-txt-check-online
```

# Usage

By default, the `carbon-txt-check-online` plugin is activated whenever you run the carbon.txt validator:
```
carbon-txt validate file https://some-domain.com/carbon.txt
```

You can then run the carbon.txt CLI command

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd carbon-txt-check-online
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

You can also use `uv`, to avoid faffing around with virtual environments:

```bash

# run uv as above
uv run carbon-txt validate file https://some-domain.com/carbon.txt
```