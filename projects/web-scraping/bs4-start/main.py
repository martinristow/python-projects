from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)  # dokolku sakame da go dobieme title
print(soup.title.name)  # ke ni vrati title bidejki toa e imeto na tagot
print(soup.title.string)  # ke ni go vrati tekstot pomegju title

print(soup.prettify())  # ni vrakja poubav izgled vo konzolata za da bide polesno za citanje

print(soup.a)  # ova ke ni go vrati prviot anchor tag(a) od dokumentot
print(soup.li)  # ova ke ni go vrati prviot li tag od dokumentot
# primer soup.p, soup.img, soup.h1, soup.h2 itn..... site ovie ni vrakjat nekoj rezultat dokolku postojat
