import re

def clean(tweet):
	tweet = re.sub('(http\S+)', '', tweet, flags=re.MULTILINE)
	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ /+ \S +) ", " ", tweet).split())




tweet = "Apple's @hello https://t.co/WY97HGHyau next iPhone may #apple have a ‘secret weapon’ https://t.co/WY97HGHyau via FOX NEWS https://t.co/WY97HGHyau Make us your Media Partner to… https://t.co/nxpd18XWck"
print(clean(tweet))