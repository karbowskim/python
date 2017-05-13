import webbrowser
import urllib.request
import re
import sys

websiteAddress = input("Enter website url: ")
textToFind = input("Enter word to search (the search is case sensitive): ")

with urllib.request.urlopen(websiteAddress) as url:
    html_content = url.read()

htmlString = html_content.decode("utf-8")

matches = re.findall(textToFind, htmlString);
stringOccurences = len(matches)

if stringOccurences != 0:
   print (str(stringOccurences) + " occurences of \'" + str(textToFind) + "\' found on: " +  str(websiteAddress))
else:
   print ("No occurences of \'" + str(textToFind) + "\' on " + str(websiteAddress))

decision = input("Would you like to visit the site? (yes/no): ")

if decision is 'yes':
    webbrowser.open(websiteAddress)
if decision is 'no':
    sys.exit()
