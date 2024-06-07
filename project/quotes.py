import requests as rq

r = rq.get("https://quotes.toscrape.com")

r.status_code

r.encoding

html = r.text

#extraindo as quotes

quotes = []
string_text = '<span class="text" itemprop="text">“'
for line in html.split('\n'):
    if string_text in line:
        line = (line.replace(string_text, '').replace('.”</span>', ''))
        line = line.strip()
        quotes.append(line)

with open('quotes.txt', 'w',encoding='utf-8') as f:
    for quote in quotes:
        f.write(quote + '\n')
        

#extraindo o nome dos autores

authors = []
string_author = '<small class="author" itemprop="author">'
for line in html.split('\n'):
    if string_author in line:
        line = (line.replace(string_author, '')).replace('</small>', '').replace('<span>by ','')
        line = line.strip()
        authors.append(line)

with open('authors.txt', 'w',encoding='utf-8') as f:
    for author in authors:
        f.write(author + '\n')

     
#fazendo paginação para quotes

for page in range(1,11):
    r = rq.get("https://quotes.toscrape.com/page/" + str(page), timeout=5)
    html = r.text
    quotes = []
    string_text = '<span class="text" itemprop="text">“'
    for line in html.split('\n'):
        if string_text in line:
            line = (line.replace(string_text, '').replace('.”</span>', ''))
            line = line.strip()
            quotes.append(line)
    with open('quotes_10_pages.txt', 'a',encoding='utf-8') as f:
        f.write('\n'+'Pagina '+str(page) + '\n')
        for quote in quotes:
            f.write(quote + '\n')

#fazendo paginação para autores

for page in range(1,11):
    r = rq.get("https://quotes.toscrape.com/page/" + str(page), timeout=5)
    html = r.text
    authors = []
    string_author = '<small class="author" itemprop="author">'
    for line in html.split('\n'):
        if string_author in line:
            line = (line.replace(string_author, '')).replace('</small>', '').replace('<span>by ','')
            line = line.strip()
            authors.append(line)
    with open('authors_10_pages.txt', 'a',encoding='utf-8') as f:
        f.write('\n'+'Pagina '+str(page) + '\n')
        for author in authors:
            f.write(author + '\n')

#criando arquivo com "author,quote" extraidos do site e salvando em csv

for page in range(1,11):
    r = rq.get("https://quotes.toscrape.com/page/" + str(page), timeout=5)
    html = r.text
    authors = []
    quotes = []
    string_author = '<small class="author" itemprop="author">'
    string_quotes = '<span class="text" itemprop="text">“'
    for line in html.split('\n'):
        if string_author in line:
            line = (line.replace(string_author, '')).replace('</small>', '').replace('<span>by ','')
            line = line.strip()
            authors.append(line)
        if string_quotes in line:
            line = (line.replace(string_quotes, '').replace('.”</span>', ''))
            line = line.strip()
            quotes.append(line)
    with open('authors_quotes.csv', 'a',encoding='utf-8') as f:
        for author,quote in zip(authors,quotes):
            f.write(author + ',' + quote + '\n')

