# Donation Manager
DonationManager is a python package for interacting with the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) to retrive donation information.
The API is used with several non-profits (namely [Extralife](https://www.extra-life.org/home)) to track and output donation information from a participant's fundraising page.

## Getting started 

>[!NOTE]
> As said in the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) documentation, please limit requests from the API (and by extension this package) to every 15 seconds.
>
> Methods that make calls to the API currently include `get_new_donations()`, `_request_donos()`, and `_output_to_file()` (if no json data is explicitly given as it calls `_request_donos()`)

### Building module from source
> [!IMPORTANT] 
> Currently building from source locally is the only method to use this package, until I get around to publishing the package to PyPi (if I ever do)

Download the latest source code for this file from github using git 
```bash
git clone https://github.com/jp8fluffy/DonorDrive-Python-API.git
``` 
or by downloading the zip off github. 
Extract the zip file if downloaded. 

#### Installing to other projects
Setup your python project as normal
Create and enter your project's virtual environment using the built-in [python venv method](https://docs.python.org/3/library/venv.html) or using an external virtual environment manager (like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)).
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
