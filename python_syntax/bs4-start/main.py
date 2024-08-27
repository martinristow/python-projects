from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
print(soup.title)  # dokolku sakame da go dobieme title
print(soup.title.name)  # ke ni vrati title bidejki toa e imeto na tagot
print(soup.title.string)  # ke ni go vrati tekstot pomegju title
#
print(soup.prettify())  # ni vrakja poubav izgled vo konzolata za da bide polesno za citanje
#
print(soup.a)  # ova ke ni go vrati prviot anchor tag(a) od dokumentot
print(soup.li)  # ova ke ni go vrati prviot li tag od dokumentot
# primer soup.p, soup.img, soup.h1, soup.h2 itn..... site ovie ni vrakjat nekoj rezultat dokolku postojat

all_anchor_tags = soup.findAll(name="a")  # ke gi dobieme site anchor_tags so pomos na funkcijata findall
# i go navedeme imeto na tagot vo nasiot slucaj name="a"

for tag in all_anchor_tags:
    print(tag.getText())  # go vadime tekstot od anchor tagot
    print(tag.get("href"))  # gi dobivame site linkovi od href
    # pass

heading = soup.find(name="h1", id="name")  # mozeme da izolirame nekoj element posebno
# primer samo ni treba eden h1 a ne site ostanati h1 i so pomos na id-to mu pristapuvame na toj element
print(heading)

section_heading = soup.find(name="h3", class_="heading")  # na ovoj nacin mozeme da pristame i do nekoja klasa od html
# dokumentot samo class ne mozeme da koristime bidejki toj e predefiniran zbor
# i namesto nego koristime class_ pa imeto na klasata vo html dokumentot
print(section_heading.name) # ke ni vrati h3
print(section_heading.get("class")) # ke ni go vrati imeto na klasata

name = soup.select_one(selector="#name") # na ovoj nacin kako koga selektirame nekoj element preku css
# mozeme i tuka da selektirame nekoj element so pomos na select i select_one vo zavisnost
# od toa kolku elementi ni se potrebni i slicno
print(name)

headings = soup.select(".heading") # dobivame lista od site elementi koj sto go sodrzat imeto na klasata heading
print(headings)

