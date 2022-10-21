import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #asks for the user_name of a twitter account
    print('')
    acct = input('Enter Twitter Account:')
    # if whats input into the terminal has a len count
    # less than 0 quit the loop
    if (len(acct) < 1): break
    
    # makes a URL and does all the signing with the keys and all
    # the count number means that it will return 5 users
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '100'})
    print('Retrieving', url)
    
    # This pulls the information and  decodes the information
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    
    # this parses the java script into a list
    js = json.loads(data)
    
    #debug pretty print
    print(json.dumps(js, indent=4)[:250])

    # brings you back the headers #and with the headers you can look through it
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    
    # JS is a dictionary
    # JS sub 'users' is a list
    for u in js['users']:
        # this is gonaa be the first person on the list
        # and gets the screen name
        print(u['screen_name'])
        
        # if theres no status print this
        if 'status' not in u:
            print('   * No status found')
            continue
        # searches through the users status then geoes to the text
        # and prints the first 50 characters
        s = u['status']['text']
        print('  ', s[:50])