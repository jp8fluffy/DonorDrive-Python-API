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
            with open(self.path_to_json, "a") as file:
                empty_json = '{}'
                file.write(empty_json)
        except OSError as e:
            print(f"Error creating json file {self.path_to_json}: {e}")

    def _request_donos(self):
        # request donoations from extralife, convert from html to json and return
        dono_api_request = self.scraper.get(self.url)
        dono_json = json.loads(dono_api_request.text)
        return dono_json

    def _output_to_file(self, json_data):
        # Check for an already existing json file, if none exists, create a new one
        try:
            # Checks for json file existance
            abs_path_to_json = self.path_to_json.resolve(strict=True)
        except FileNotFoundError:
            # File does not exist
            print('File does not exist... creating json file')
            self._create_donos_json()
            with open(self.path_to_json, 'w') as file:
                file.write(json.dumps(json_data, indent=4))
        else:
            # File exists
            with open(abs_path_to_json, 'w') as file:
                file.write(json.dumps(json_data, indent=4))

    
    def get_new_donations(self):
        stored_donation_data = self._load_json_file()
        new_donation_data = self._request_donos()
        
        amount_of_new_donations = len(new_donation_data) - len (stored_donation_data)

        if amount_of_new_donations > 0:
            new_donations_json = new_donation_data[0:amount_of_new_donations]
            self._output_to_file(new_donation_data)
            return [amount_of_new_donations, new_donations_json]
        elif amount_of_new_donations < 0:
            raise ValueError(f'New donations are smaller than stored donations ({amount_of_new_donations=})')
        else:
            empty_json = '{}'
            return [amount_of_new_donations, empty_json]
            
            
    def _load_json_file(self, filepath=None, max_attempts=3):
        attempts = 0

        while attempts < max_attempts:
            if filepath is not None:
                try:
                    with open(filepath, 'r') as json_file:
                        stored_donation_data = json.load(json_file)
                    return stored_donation_data
                except FileNotFoundError:
                    print('Json file not found; Creating new json file...')
                    self._create_donos_json()
                    attempts += 1
            else:
                try:
                    with open(self.path_to_json, 'r') as json_file:
                        stored_donation_data = json.load(json_file)
                    return stored_donation_data    
                except FileNotFoundError:
                    print('Json file not found; Creating new json file...')
                    self._create_donos_json()
                    attempts += 1

        if attempts == max_attempts:
            raise RuntimeError('Could not load specified file and could not create new file')




