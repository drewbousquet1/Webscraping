import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

ran_num = random.randrange(1,21)
if ran_num < 10:
    ran_num = '0' + str(ran_num)
else:
    ran_num = str(ran_num)


webpage = 'https://ebible.org/asv/JHN' + ran_num + '.htm'
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)
page = urlopen(webpage)
soup = BeautifulSoup(page, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div',class_='p')

my_verses = []

for section_verse in page_verses:
    verse_list = section_verse.text.split(".")
   
    for v in verse_list:
        my_verses.append(v)

    my_verses = [i for i in my_verses if i != ' ']
    my_choice = random.choice(my_verses)

    print(f"Chapter: {ran_num} Verse: {my_choice}")
    
    



