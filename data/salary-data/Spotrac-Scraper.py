from lxml import html
import requests
import os
import csv

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]

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
	'utah-jazz' : 'UTH', 'washington-wizards' : 'WAS'
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


	players = tree.xpath('//tr/td//text()')
	lst = list(range(len(players)))
	
	totsalaries = []
	numTotsalaries = []
	salaries = []
	numberSalaries = []
	names = []
	positions = []
	teams = []
	ages = []
	status = []

	for i in lst:
		if players[i] in teamsDictionary.values() and players[i+1] in teamsDictionary.values():
			if players[i-3] in positionsDictionary.values():	
				if  len(players[i+3]) > 2:
					names.append(players[i-4])
					salaries.append(players[i+4])
					totsalaries.append(players[i+3])
					ages.append(players[i-2])
					status.append(players[i-1])
					positions.append(players[i-3])
					teams.append(players[i])
	# print(len(names))

	
	with open(str(year) + ".csv", 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ',')
		filewriter.writerow(['last name', 'first name', 'age', 'position', 'team', 'faStatus', 'total-contract', 'average'])
	
	for salary in salaries:
		s = salary.replace("$","")
		s = s.replace(",","")
		s = s.replace(" ","")
		k = int(s)
		numberSalaries.append(k)

	for totsalary in totsalaries:
		s = totsalary.replace("$","")
		s = s.replace(",","")
		s = s.replace(" ","")
		k = int(s)
		numTotsalaries.append(k)

	#  print(sum(numTotsalaries))
	
	with open(str(year) + ".csv", 'a') as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ',')
		for i in range(len(names)):
			fullName = names[i].split(" ")
			first = ""
			middle = ""
			last = ""

			first = fullName[0]
			if (len(fullName) == 3) :
				middle = fullName[1]
				last = fullName[2]
			else :
				last = fullName[1]

			filewriter.writerow([middle + last, first, ages[i], positions[i], teams[i], status[i], numTotsalaries[i], numberSalaries[i]])
	




