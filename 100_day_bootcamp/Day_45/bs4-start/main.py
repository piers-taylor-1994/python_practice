from bs4 import BeautifulSoup
import requests

# with open("Day 45/bs4-start/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.li)

# list = soup.find_all(name="a")
# for l in list:
#     print(l.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# heading3 = soup.find(name="h3", class_="heading")
# print(heading3)

# company_url = soup.select_one(selector="body p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)

# web_page = requests.get("https://news.ycombinator.com/news")
# web_page = web_page.text

# soup = BeautifulSoup(web_page, "html.parser")

# articles = soup.select(".titleline a")
# # article_tag = soup.find(name="a")^

# article_texts = []
# articles_links = []
# skip = False

# for article_tag in articles:
#     text = article_tag.getText()
#     if not skip:
#         article_texts.append(text)

#     link = article_tag.get("href")
#     articles_links.append(link)
#     skip = not skip

# article_upvotes = [int(score.getText().split()[0]) for score in soup.select(".score")]
# # article_upvote = soup.find(name="span", class_="score")^

# highest_upvotes = max(article_upvotes)
# index_of_highest_upvotes = article_upvotes.index(highest_upvotes)

# print(article_upvotes)

# print(article_texts[index_of_highest_upvotes])
# print(articles_links[index_of_highest_upvotes])
# print(article_upvotes[index_of_highest_upvotes])

site = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
site = site.text

soup = BeautifulSoup(site, "html.parser")
titles = [t.getText() for t in soup.select(".article-title-description .article-title-description__text .title")[::-1]] 
# titles = [t.getText() for t in soup.find_all(name="h3", class_="title")[::-1]] ^Interchangeable
titles_text = ""

for t in titles:
    titles_text += f"{t}\n"

with open("Day 45/bs4-start/movies.txt", mode="w", encoding="utf-8") as file:
    file.write(titles_text)