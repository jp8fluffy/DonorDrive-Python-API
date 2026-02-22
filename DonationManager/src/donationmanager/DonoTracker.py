from html_to_json import convert as convert_to_json
from pathlib import Path
import cloudscraper
import json


class DonationTracker():
    # Class for getting and storing donations 
    def __init__(self, url, filename='donos.json') -> None:
        # Set url to get api requests and creates a new cloudscraper object (to get requests from cloudflare server) 
        self.url = url
        self.scraper = cloudscraper.create_scraper()

        # Uses filename (if given) to set path to the json file with donation information
        # Otherwise uses default path (local and named donos.json)
        self.filename = filename
        self.path_to_json = Path(filename)

        # Create json file unless it already exsists
        self._create_donos_json()

    def _create_donos_json(self):
        try:
            self.path_to_json.touch()
        except FileExistsError:
            print('Json file already exists')

    def _request_donos(self):
        # request donoations from extralife, convert from html to json and return
        dono_api_request = self.scraper.get(self.url)
        dono_json = json.loads(dono_api_request.text)
        return dono_json

    def _output_to_file(self):
        # Check for an already existing json file, if none exists, create a new one
        try:
            # Checks for json file existance
            abs_path_to_json = self.path_to_json.resolve(strict=True)
        except FileNotFoundError:
            # File does not exist
            print('File does not exist... creating json file')
            self._create_donos_json()
            with open(self.path_to_json, 'w') as file:
                file.write(json.dumps(self._request_donos(), indent=4))
        else:
            # File exists
            with open(abs_path_to_json, 'w') as file:
                file.write(json.dumps(self._request_donos(), indent=4))

    
    # def get_new_donations(self):

