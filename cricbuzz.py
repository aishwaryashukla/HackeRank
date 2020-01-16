from pycricbuzz import Cricbuzz
import json
import pprint

c = Cricbuzz()

matches = c.matches()
for match in matches:
	print(match)
	if(match['mchstate'] != 'nextlive'):
		print(c.scorecard(match['id']))
