import os
import sys
import csv

column = {}


def defineTitle(header):
    index = 0
    for title in header:
        column[title] = index
        index+=1

def main(args):
    print args[1]
    filePointer = open(args[1], 'r')
    reader = csv.reader(filePointer, delimiter=',')
    header = reader.next()
    defineTitle(header)
    print column
#    for row in reader:
 #       print row
    filePointer.close()
    return

"""
body1 = Defect Description
In the "Vibration Control" experiment, the minimum requirement to run the experiment is not displayed in the page instead a page or Scrolling should appear providing information on minimum requirement to run this experiment, information like Bandwith,Device Resolution,Hardware Configuration and Software Required.

Actual Result :
In the "Vibration Control" experiment, the minimum requirement to run the experiment is not displayed in the page.     

Environment :
OS: Windows 7,Linux
Browsers: Firefox,Chrome
Bandwidth : 100Mbps
Hardware Configuration:8GBRAM
Processor:i

body2 = "Defect Description\nTest multiple lines comment"

curl = curl -i -H 'Authorization: token ba89586c2af27b18c180f4fb346bbba838532395' -d '{ "title": "QA_Defect_Structural Dynamics_100", "body": "%s", "labels": ["S2"]}' https://api.github.com/repos/ayogi/import-github-issues/issues
%(body2)

print curl

os.system(curl)

Labels:
status -> status
date -> start date
"""

if __name__ == "__main__":
    main(sys.argv)
