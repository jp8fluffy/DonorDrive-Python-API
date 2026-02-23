# Donation Manager
DonationManager is a python package for interacting with the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) to retrive donation information.
The API is used with several non-profits (namely [Extralife](https://www.extra-life.org/home)) to track and output donation information from a participant's fundraising page.

>[!NOTE]
> As said in the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) documentation, please limit requests from the API (and by extension this package) to every 15 seconds.
>
> Methods that make calls to the API currently include `get_new_donations()`, `_request_donos()`, and `_output_to_file()` (if no json data is explicitly given as it calls `_request_donos()`)

# Getting started 
## Building module from source
> [!NOTE] 
> Currently building from source locally is the only method to use this package, until I get around to publishing the package to PyPi (if I ever do)

Download the latest source code for this file from github using git `git clone https://github.com/jp8fluffy/DonorDrive-Python-API.git` or by downloading the zip off github. 
Extract the zip file if downloaded. 

### Installing to other projects
Setup your python project as normal
Create and enter your project's virtual environment using the built-in [python venv method](https://docs.python.org/3/library/venv.html) or using an external virtual environment manager (like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html))
Navigate to DonationManager's `src/` directory then run `python3 -m pip install -e .` or by running `python3 -m pip install -e <PATH-TO-DOWNLOAD>/DonorDrive-Python-API/DonationManager/src`
This should install the package and it's dependencies into your python project

# Usage
## Importing
Find the link to your API link for your donations (For help finding your link go to [Donor Drive API: How tos](https://github.com/DonorDrive/PublicAPI/blob/master/how-tos.md))
Import the module into your python project as normal
> [!IMPORTANT]
> Currently the import is fairly messy, and has to be imported a little confusingly, see the example code below
## Creating a new Donation Manager class
After importing the DonationTracker class can be initialized like any other python object, requiring a url to your [DonorDrive donation API Link](https://github.com/DonorDrive/PublicAPI/blob/master/how-tos.md)

Optionally, after the URL, a second string giving the name for the json file. The format is `<PATH>/<FILENAME>.json` inputting any other filetype into the method raises a TypeError

## Using the get_new_donations() method
Any DonationTracker object can get the `get_new_donations()` method. Calling this method requests the donation Json from the Donor Drive API for the participant's link
> [!IMPORTANT]
> As stated above, Donor Drive's API kindly asks that you only make a request from the API every [15 seconds](https://github.com/DonorDrive/PublicAPI)

The method calls the API, which returns JSON data. 
It then checks if there is already a local donos.json 
The return from this method is an array of the format [number of new donations, new donations json]
The Json returned **in the array** is formatted as a **python dictionary inside of an array** this is a little strange, however it is a byproduct of Python's built-in [Json Handler Module](https://docs.python.org/3/library/json.html).
This format allows interchangability between Json (for file handling) and usage in python. It is essential the formatting is not changed, as doing so may lead to malformed JSON file output.
An example of the output of this is as follows
```python
[1, [{'displayName': 'Johnpaul Shields', 'donorID': '79D83C498A38FBB3', 'links': {'recipient': 'https://www.extra-life.org/participants/566838', 'donate': 'https://www.extra-life.org/participants/566838/donate'
}, 'isRegFee': False, 'eventID': 562, 'createdDateUTC': '2026-02-20T21:14:29.923Z', 'recipientName': 'Johnpaul Shields', 'recipientImageURL': 'https://donordrivecontent.com/extralife/images/$avatars$/constituen
t_E4B21B29-DD36-DBF8-79D83C498A38FBB3.jpg?v=1771442940259', 'message': 'Test Dono 2', 'participantID': 566838, 'amount': 1.0, 'donorIsRecipient': True, 'avatarImageURL': 'https://donordrivecontent.com/extralife
/images/$avatars$/constituent_E4B21B29-DD36-DBF8-79D83C498A38FBB3.jpg?v=1771442940259', 'donationID': '235890E3214394E3'}]]
```
The method then writes the new data to the json file allowing the method to be used again.
When no new donations are given, the method returns `[0, '{}']` of which `'{}'` is an empty json list

# Example of Usage
```python
from donationmanager import DonoTracker

url = 'https://www.extra-life.org/api/1.6/participants/minismeef/donations'
donotracker = DonoTracker.DonationTracker(url)

if __name__ == '__main__':
    new_donations = donotracker.get_new_donations()
    print(new_donations)
```
    
# Dependancies
- Latest version of [Python3](https://www.python.org/downloads/)
- [CloudScraper](https://github.com/VeNoMouS/cloudscraper) (>=1.2.71,<2.0.0)
- [poetry-core](https://python-poetry.org/) >=2.0.0,<3.0.0 used for building package
