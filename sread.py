import json

with open('se.json','r') as f:
	line = f.readline() # read only the first tweet/line
	#tweet = json.loads(line) # load it as Python dict
	#print(json.dumps(tweet, indent=4)) # pretty-print
	cnt = 1
	while line:
		if len(line) > 1:
			obj = json.loads(line)
			print(obj['place']['country'] if obj['place'] else "-")
			cnt += 1
		line = f.readline()