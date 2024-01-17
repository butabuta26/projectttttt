import requests
import csv
from bs4 import BeautifulSoup

column_name = ['Entry Number', 'Name', 'Year', 'Movie Rating', 'Directed by']
csvfile = open('tomato_movies.csv', 'w', newline='', encoding='utf-8')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(column_name)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

website = requests.get('https://editorial.rottentomatoes.com/guide/popular-movies/', headers=headers).text
soup = BeautifulSoup(website, 'lxml')

movies = soup.find_all('div', class_= 'row countdown-item')
c = 0

