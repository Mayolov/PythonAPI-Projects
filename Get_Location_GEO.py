import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# asks for location
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    
    # takes the key and value so that it encodes it into the URL
    # its a string that concatenates to the end of the url
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    uh = urllib.request.urlopen(url, context=ctx)
    
    # turns it into unicode
    data = uh.read().decode()
    
    # retrieves the characters 
    print('Retrieved', len(data), 'characters')
    
    # with json you parse the data and if it blows up
    # it goes through the except function
    try:
        # this makes a dictionary
        js = json.loads(data)
    except:
        js = None

    # if we got a false or none itll quit
    # if theres no status key it will quit
    # if its not equal to ok it will quit
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    # opposite of loadS
    # takes the dictionary that includes arrays and
    # prints it out nicely with the indenation of 4
    print(json.dumps(js, indent = 4))
    
    # results is the first key and that is a dictonary
    # this is a dictionary within a dictionary within a dictiony
    # and gets both for lat and lng
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    
    print('lat', lat, 'lng', lng)
    
    location = js['results'][0]['formatted_address']
    print(location)