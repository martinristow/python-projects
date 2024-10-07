from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = 'https://www.nba.com/stats/teams'

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url=URL, headers=header)
nba_website_html = response.text

soup = BeautifulSoup(nba_website_html, 'html.parser')
# print(soup.prettify())

nba_parts = soup.findAll(class_='StatsTeamsList_divName__HMBNq')
nba_teams = soup.findAll(class_='StatsTeamsList_team__xE5KF')

parts = [part.text for part in nba_parts]
teams = [team.text for team in nba_teams]

chunked_teams = []
temp_list = []

for i, team in enumerate(teams):
    temp_list.append(team)
    if (i+1) % 5 == 0:
        chunked_teams.append(temp_list)
        temp_list = []

# print(parts)
# print(chunked_teams)

data = {}

for i, item in enumerate(parts):
    # print(item)
    data[item] = []
    for j in range(len(chunked_teams[i])):
        data[item].append(chunked_teams[i][j])
        # print(chunked_teams[i][j])
    # print('\n')

df = pd.DataFrame.from_dict(data, orient='index').transpose()

df.to_csv('nba_teams_data.csv', index=False)

print("Data has been written to nba_teams_data.csv")
