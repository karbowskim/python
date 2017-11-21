import webbrowser
import requests
import re
import sys

websiteAddress = input("Enter website url: ")
textToFind = input("Enter word to search (the search is case sensitive): ")

html_content = requests.get(websiteAddress).text

matches = re.findall(textToFind, html_content)
stringOccurences = len(matches)

if stringOccurences != 0:
   print (str(stringOccurences) + " occurences of \'" + str(textToFind) + "\' found on: " +  str(websiteAddress))
else:
   print ("No occurences of \'" + str(textToFind) + "\' on " + str(websiteAddress))

decision = input("Would you like to visit the site? (y/n): ")

if decision == 'y':
    webbrowser.open(websiteAddress)
if decision == 'n':
    sys.exit()
