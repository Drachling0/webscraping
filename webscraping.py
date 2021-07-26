# source website: https://www.numbeo.com/cost-of-living/

# Beispiel (auf Englisch): 
# 
# Food: Eggs
#
# Which cities do you want to compare?
# 1. Berlin
# 2. Munich


from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    food = input("Food: ").capitalize()
    city_1 = input("Which cities do you want to compare? \n1. ").capitalize()
    city_2 = input("2. ").capitalize()

    url = f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table',attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})
    rows = table.find_all('tr')
    

    def function(): 
        i = 0
        while i < len(rows):
            if food in str(rows[i]):
                print("Found!")
                return rows[i]
            i+= 1

    food_data = function().text.split()

    indices = [index for index, char in enumerate(food_data) if char == '€']

    price_1 = food_data[indices [0] - 1]
    price_2 = food_data[indices [1] - 1]

print('The price of ' + food + f' in {city_1} is {price_1}€')
print('The price of ' + food + f' in {city_2} is {price_2}€')