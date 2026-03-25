from donationmanager import DonoTracker
import json

url = "https://www.extra-life.org/api/1.6/participants/minismeef/donations"
donotracker = DonoTracker.DonationTracker(url)

if __name__ == "__main__":
    print("get_new_donations output:")
    new_donations = donotracker.get_new_donations()
    print(json.dumps(new_donations, indent=4))
