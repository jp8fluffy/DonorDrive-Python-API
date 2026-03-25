from donationmanager import DonoTracker
import json

url = "https://www.extra-life.org/api/1.6/participants/minismeef/donations"
donotracker = DonoTracker.DonationTracker(url)

if __name__ == "__main__":
    print("get_cached_donation(0) output:")
    last_donation = donotracker.get_cached_donation(0)
    print(json.dumps(last_donation, indent=4))

    print("get_cached_donation(1) output:")
    donation_1 = donotracker.get_cached_donation(1)
    print(json.dumps(donation_1, indent=4))

    print("out of bounds donation output:")
    donation_out_of_bounds = donotracker.get_cached_donation(999)
    print(json.dumps(donation_out_of_bounds, indent=4))

    print("non-int index donation output:")
    donation_non_int = donotracker.get_cached_donation("1")
    print(json.dumps(donation_non_int, indent=4))
