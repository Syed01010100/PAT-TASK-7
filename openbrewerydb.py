import requests
from collections import Counter

url_ny = "https://api.openbrewerydb.org/v1/breweries?by_state=new+york"
url_maine = "https://api.openbrewerydb.org/v1/breweries?by_state=maine"
url_alaska = "https://api.openbrewerydb.org/v1/breweries?by_state=alaska"

def fetch_brewery_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # check http error
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def main():

    ny_breweries = fetch_brewery_data(url_ny) # fetch breweries for each state from data
    maine_breweries = fetch_brewery_data(url_maine)
    alaska_breweries = fetch_brewery_data(url_alaska)

    if ny_breweries is not None and maine_breweries is not None and alaska_breweries is not None:

        all_breweries = ny_breweries + maine_breweries + alaska_breweries # make it one list for all breweries


        print("List of all breweries:") # print all breweries
        for brewery in all_breweries:
            print(brewery['name'])


        print("The count of breweries in each of the states :")
        print("New York:", len(ny_breweries))
        print("Maine:", len(maine_breweries))
        print("Alaska:", len(alaska_breweries))

        # Count types of breweries
        brewery_types = [brewery['brewery_type'] for brewery in all_breweries]
        brewery_types_count = Counter(brewery_types)
        print("number of types of breweries :", brewery_types_count)

        # Count how many breweries have websites
        website_count = sum(1 for brewery in all_breweries if 'website_url' in brewery)
        print("Count :", website_count)
    else:
        print("Could not fetch brewery data.")

if __name__ == "__main__":
    main()