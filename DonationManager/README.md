## Usage
### Importing
Find the link to your API link for your donations (For help finding your link go to [Donor Drive API: How tos](https://github.com/DonorDrive/PublicAPI/blob/master/how-tos.md)).
Import the module into your python project as normal

> [!IMPORTANT]
> Currently the import is fairly messy, and has to be imported a little confusingly, see the example code below

### Creating a new Donation Manager class
After importing the DonationTracker class can be initialized like any other python object, requiring a url to your [DonorDrive donation API Link](https://github.com/DonorDrive/PublicAPI/blob/master/how-tos.md)

Optionally, after the URL, a second string giving the name for the json file. The format is `<PATH>/<FILENAME>.json` inputting any other filetype into the method raises a TypeError

### Using the get_new_donations() method
Any DonationTracker object can get the `get_new_donations()` method. Calling this method requests the donation Json from the Donor Drive API for the participant's link

The method calls the API, which returns JSON data. 
It then checks if there is already a local donos.json. 
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

## Example of Usage
```python
from donationmanager import DonoTracker

url = 'https://www.extra-life.org/api/1.6/participants/minismeef/donations'
donotracker = DonoTracker.DonationTracker(url)

if __name__ == '__main__':
    new_donations = donotracker.get_new_donations()
    print(new_donations)
```
