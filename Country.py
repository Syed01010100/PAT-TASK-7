import requests

class Countries:
    def __init__(self, url):
        self.url = url
        self.data = self.get_json_data()  # data fetch during init.

    def get_json_data(self):
        try:
            response = requests.get(self.url, verify=False)  # create a request
            response.raise_for_status()  # check if okey
            return response.json()  # return it
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)  # print error if any occur
            return None  # return none if no error

    def get_countries_with_currency(self, currency_code):
        if self.data is None:  # check fetching data if okey
            return []  # return empty list

        countries = []  # init. emty list to store country
        for country in self.data:  # for statement for each country in data
            if 'currencies' in country and currency_code in country['currencies']:  # check currency
                countries.append(country['name']['common'])  # add country name is list
        return countries


country_data = Countries("https://restcountries.com/v3.1/all")


dollar_countries = country_data.get_countries_with_currency('USD')
print("Countries that use Dollar as currency:", dollar_countries)


euro_countries = country_data.get_countries_with_currency('EUR')
print("Countries that use Euro as currency:", euro_countries)