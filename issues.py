import os
import sys
import csv
import json

column = {}
token = "a2bf7f64bd62187791b092989823f4dc16310cc8"
githubUrl = "https://api.github.com/repos/ayogi/import-github-issues/issues"

def defineTitle(header):
    index = 0
    for title in header:
        column[title] = index
        index+=1
   return

def printIssue(reader):
    issueNumber = 1
    for row in reader:
        if issueNumber >= 5:
            break
        print issueNumber, row[column["Description"]],
        issueNumber+=1
    return

def createIssue(row):
    dictionary = {}
    dictionary["title"] = row[column["Subject"]]
    dictionary["body"] = row[column["Description"]]
    dictionary["labels"] = [row[column["Status"]], row[column["Severity"]], row[column["Category"]], row[column["Assigned by"]], row[column["Release Number"]], row[column["Start date"]], row[column["Project"]]]
    jsonString = json.dumps(dictionary)
    curl = """curl -i -H 'Authorization: token %s' -d '%s' %s""" %(token, jsonString, githubUrl)
    print curl
    os.system(curl)

def main(args):
    filePointer = open(args[1], 'r')
    reader = csv.reader(filePointer, delimiter=',')
    header = reader.next()
    defineTitle(header)
#    printIssue(reader)
    row = reader.next()
    createIssue(row)
    filePointer.close()
    return

"""
['#', 'Project', 'Tracker', 'Parent task', 'Status', 'Priority', 'Subject', 'Author', 'Assignee', 'Updated', 'Category', 'Target version', 'Start date', 'Due date', 'Estimated time', '% Done', 'Created', 'Closed', 'Related issues', 'Assigned by', 'Severity', 'Category', 'Release Number', 'Developer Comments', 'Test Step No', 'Description']

curl = curl -i -H 'Authorization: token ba89586c2af27b18c180f4fb346bbba838532395' -d '{ "title": "QA_Defect_Structural Dynamics_100", "body": "%s", "labels": ["S2"]}' https://api.github.com/repos/ayogi/import-github-issues/issues
%(body2)
"""

if __name__ == "__main__":
    main(sys.argv)
