import webbrowser
import urllib.request
import re
import sys


address = input("Enter website url: ")

with urllib.request.urlopen(address) as url:
    html_content = url.read()

htmlString = html_content.decode("utf-8")

matches = re.findall('Soccerway', htmlString);
stringOccurences = len(matches)

if stringOccurences != 0:
   print ("String occured " + str(stringOccurences) + " times")
else:
   print ("String not found")

decision = input("Would you like to visit the site? (y/n): ")

if decision is 'y':
    webbrowser.open(address)
if decision is 'n':
    sys.exit()
