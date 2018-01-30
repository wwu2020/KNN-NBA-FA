from lxml import html
import requests
import os
import csv
import re

years = [2018]

teams = ['atlanta-hawks', 'boston-celtics', 'brooklyn-nets', 
	'charlotte-hornets', 'chicago-bulls', 'cleveland-cavaliers', 
	'dallas-mavericks', 'denver-nuggets', 'detroit-pistons', 
	'golden-state-warriors', 'houston-rockets', 'indiana-pacers', 
	'los-angeles-clippers', 'los-angeles-lakers', 'memphis-grizzlies', 
	'miami-heat', 'milwaukee-bucks', 'minnesota-timberwolves', 
	'new-jersey-nets', 'new-orleans-hornets', 'new-york-knicks',
	'oklahoma-city-thunder', 'orlando-magic', 'philadelphia-76ers', 
	'phoenix-suns', 'portland-trail-blazers', 'sacramento-kings', 
	'san-antonio-spurs', 'toronto-raptors',
	'utah-jazz', 'washington-wizards'
		]

teamsDictionary =  {
	'atlanta-hawks' : 'ATL', 'boston-celtics' : 'BOS', 'brooklyn-nets' : 'BKN', 'charlotte-hornets' : 'CHA', 
	'chicago-bulls' : 'CHI', 'cleveland-cavaliers' : 'CLE', 'dallas-mavericks' : 'DAL', 'denver-nuggets' : 'DEN',
	'detroit-pistons' : 'DET', 'golden-state-warriors' : 'GSW', 'houston-rockets' : 'HOU', 'indiana-pacers' : 'IND', 
	'los-angeles-clippers' : 'LAC', 'los-angeles-lakers' : 'LAL', 'memphis-grizzlies' : 'MEM', 
	'miami-heat' : 'MIA', 'milwaukee-bucks' : 'MIL', 'minnesota-timberwolves' : 'MIN', 'new-jersey-nets' : 'NJN', 
	'new-orleans-hornets' : 'NOP', 'new-york-knicks' : 'NYK','oklahoma-city-thunder' : 'OKC', 'orlando-magic' : 'ORL', 'philadelphia-76ers' : 'PHI', 'phoenix-suns' : 'PHX', 
	'portland-trail-blazers' : 'POR', 'sacramento-kings' : 'SAC', 'san-antonio-spurs' : 'SAS', 'toronto-raptors' : 'TOR',
	'utah-jazz' : 'UTH', 'washington-wizards' : 'WAS', 'unsigned' : 'TBD'
}

positionsDictionary = {
	'Point Guard' : 'PG', 'Shooting Guard' : 'SG', 'Small Forward' : 'SF', 
	'Power Forward' : 'PF', 'Center' : 'C', 'Guard' : 'G', 'Forward' : 'F'
}

for year in years:

	#Send request
	url = 'http://www.spotrac.com/nba/free-agents/' + str(year) + '/'
	page = requests.get(url)
	tree = html.fromstring(page.content)


	players = tree.xpath('//tr/td[@class= " player"]/a//text()')
	# lst = list(range(len(players)))
	
	names = list(players)
	
	# print(names)
	# print(len(names))

	
	with open(str(year) + ".csv", 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ',')
		filewriter.writerow(['name'])
	

	
	
	with open(str(year) + ".csv", 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ',')
		for i in range(len(names)):
			fixed = names[i].lower()
			fixed = re.sub('[^A-Za-z]+','',fixed)

			filewriter.writerow([fixed])
	


