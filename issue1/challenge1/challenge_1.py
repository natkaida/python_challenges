from bs4 import BeautifulSoup
import requests

def get_links():
    links = []
    with open('tasks.txt', 'r', encoding='utf-8') as file:
        for line in file:
            links.append(line.strip())
    return links

def get_imdb_link():
    for link in table.find_all('a', href=True):
        temp = link['href']
        if 'imdb' in temp:
            my_link = temp
    return my_link

def get_infobox_data():
    title = table.find_all('th', class_='plainlist')
    description = table.find_all('td', class_='plainlist')
    title_ru = table.find('th', class_='infobox-above').get_text(' ')
    title_en = table.find('td', class_='').get_text(' ')
    my_dict = {'Оригинальное название': title_en, 'В российском релизе': title_ru}

    for th, td in zip(title, description):
        t = th.get_text(' ').replace('\xa0', ' ').strip()
        d = td.get_text(' ').replace('\xa0', ' ').replace(' ,', ',').strip()
        my_dict[t] = d

    
    my_link = get_imdb_link()       
    my_dict.update(IMDb='<a href="'+ my_link +'">Страница фильма</a>')
    return my_dict 

for wiki_link in get_links():
    my_req = requests.get(wiki_link)
    soup = BeautifulSoup(my_req.content, features='lxml')
    table = soup.find('table', class_='infobox')
    fields = ['Оригинальное название', 'В российском релизе', 
              'Жанр', 'Страна', 'Режиссёр', 'В главных ролях',
              'Длительность', 'Бюджет', 'Сборы', 'IMDb']

    movie_info = '<ul>\n'

    for k, v in get_infobox_data().items():
        if k in fields:
            movie_info += f'<li><b>{k}:</b> <i>{v}</i></li>\n'
  

    with open('movies.html', 'a', encoding='utf-8') as file:
        file.write(movie_info + '</ul>\n\n')

                  
 

