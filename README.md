# Donation Manager

[![Latest Release](https://img.shields.io/github/v/release/jp8fluffy/DonorDrive-Python-API?style=flat-square&label=Release)](https://github.com/jp8fluffy/DonorDrive-Python-API/releases)

DonationManager is a python package for interacting with the
[Donor Drive API](https://github.com/DonorDrive/PublicAPI)
to retrieve donation information.
The API is used with several non-profits (namely
[Extralife](https://www.extra-life.org/home))
to track and output donation information from a participant's fundraising page.

- [Getting Started](#getting-started)
- [Installation](#installation)
  - [Install with Pip](#installing-module-from-pip)
  - [Build from source](#building-module-from-source)
- [Usage](./DonationManager/README.md)
- [Dependencies](#dependencies)

## Getting started

1. [Download Python](https://www.python.org/downloads/) _This project is written
   in the most recent version of python at the time of release (currently Python 3.14.3)_
2. Create a
   [python virtual environment](https://docs.python.org/3/library/venv.html)
   \*or use an external environment manager like
   [Conda](https://anaconda.org/channels/anaconda/packages/conda/overview)
3. Install the module from [pip](#installing-module-from-pip) or [from source](#building-module-from-source)

> [!NOTE]
> As said in the [Donor Drive API](https://github.com/DonorDrive/PublicAPI)
> documentation, please limit requests from the API (and by extension this
> package) to every 15 seconds.
> Methods that make calls to the API currently include `get_new_donations()`,
> `_request_donos()`, and `_output_to_file()` (if no json data is explicitly
> given as it calls `_request_donos()`)

## Installation

### Installing module from pip

It has finally been done! To install the module from pip, enter your virtual
environment and then run the command

```bash
pip install donationmanager
```

### Building module from source

Download the latest source code for this file from github using git

```bash
git clone https://github.com/jp8fluffy/DonorDrive-Python-API.git
```

or by downloading the zip off github.
Extract the zip file if downloaded.

#### Installing to other projects

Setup your python project as normal
Create and enter your project's virtual environment using the built-in
[python venv method](https://docs.python.org/3/library/venv.html) or using an
external virtual environment manager (like
[Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)).
Navigate to DonationManager's `src/` directory then run

```bash
python3 -m pip install -e .
```

or by running

```bash
python3 -m pip install -e <PATH-TO-DOWNLOAD>/DonorDrive-Python-API/DonationManager/.
```

This should install the package and it's dependencies into your python project

## Dependencies

- Latest version of [Python3](https://www.python.org/downloads/) (<=3.14.2)
- [CloudScraper](https://github.com/VeNoMouS/cloudscraper) (>=1.2.71,<2.0.0)
- [poetry-core](https://python-poetry.org/) >=2.0.0,<3.0.0 used for building package
