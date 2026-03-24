from donationmanager import DonoTracker

url = "https://www.extra-life.org/api/1.6/participants/minismeef/donations"
donotracker = DonoTracker.DonationTracker(url)

if __name__ == "__main__":
    print("get_last_donation output:")
    last_donation = donotracker.get_last_cached_donation()
    print(last_donation)
