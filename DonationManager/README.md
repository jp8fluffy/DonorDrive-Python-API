# Donation Manager
---
DonationManager is a python package for interacting with the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) to retrive donation information.
The API is used with several non-profits (namely [Extralife](https://www.extra-life.org/home)) to track and output donation information from a participant's fundraising page.

As said in the [Donor Drive API](https://github.com/DonorDrive/PublicAPI) documentation, please limit requests from the API (and by extention this package) to every 15 seconds.

Methods that make calls to the API currently include `get_new_donations()`, `_request_donos()`, and `_output_to_file()` (if no json data is explicitly given as it calls _request_donos())

# Dependancies
- Latest version of [Python3](https://www.python.org/downloads/)
- [CloudScraper](https://github.com/VeNoMouS/cloudscraper)
