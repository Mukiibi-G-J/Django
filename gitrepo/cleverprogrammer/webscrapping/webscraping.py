import pandas as pd
import requests
from bs4 import BeautifulSoup  
 
#then we get the url 
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.053570000000036&lon=-118.24544999999995#.YK8QE3UzbH4')
soup = BeautifulSoup(page.content, 'html.parser')
   # print(soup)

# use to  find the all  html and css classes, ids
   # print(soup.find_all('a'))

# to access a specific div with id
week = soup.find(id='seven-day-forecast-body')      
   # print(week)
   # print(week.find('li'))
items=week.find_all(class_='tombstone-container')
    # print(items)
    # print(items[0])
# trying to access the item at index 0 and access the p tag from the id 'period-name' and the find the text with the method .get_text()
print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names=[item.find(class_='period-name').get_text() for item in items ]
short_description=[item.find(class_='short-desc').get_text() for item in items]
temperater=[item.find(class_='temp').get_text() for item in items]
print(temperater)
print(short_description)
print(period_names) 

# So we use the pandas library to table the data and dictionary key is the heading of give colomu
weather_stuf= pd.DataFrame(
    {'period':period_names,
    'descriptions':short_description,
    'temperatures':temperater,
    }
)

print(weather_stuf)

weather_stuf.to_csv('weather.csv' )
