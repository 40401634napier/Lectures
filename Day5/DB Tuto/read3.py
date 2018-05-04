import urllib2, json, base64
accesstoken = "WR4BQMCM3EED1ZY7EHRA"
institution = "10007772"
page = 0
course = "U56119"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(institution, course)
request = urllib2.Request(url)
request.add_header("Authorization", "Basic " + base64.encodestring(accesstoken+":").replace('\n',''))
response = urllib2.urlopen(request)
data = json.load(response)
print json.dumps(data, indent=2)
