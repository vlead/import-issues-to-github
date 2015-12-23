import os
import sys
import csv
import json
import urllib
from config import *

column = {}

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

def postRequest(curl):
    os.system(curl)
    return

def createIssue(row):
    dictionary = {}
    project = row[column["Project"]]
    experimentName = row[column["Experiment name"]]
    feature = row[column["Feature"]]
    testStepNum = row[column["Test Step No"]]
    testStepNum = testStepNum.zfill(2)
    subject = "QA_%s_%s" %(experimentName, feature)

    explink = urllib.quote(experimentName)
    link =  "https://github.com/%s/%s/blob/master/test-cases/integration_test-cases/%s/%s_%s_%s.org" %(organization, project, explink, explink, testStepNum, feature) 
    description = row[column["Description"]] + "\n Test Step Link:\n%s" %(link)

    statusLabel = "Status: " + row[column["Status"]]
    severityLabel = "Severity: " + row[column["Severity"]]
    categoryLabel = "Category: " + row[column["Category"]]
    assignedByLabel = "Assigned by: " + row[column["Assigned by"]]
    releaseNumLabel = "Release Number: " + row[column["Release Number"]]
    dateLabel = "Start Date: " + row[column["Start date"]]
    projectLabel = "Project: " + row[column["Project"]]

    dictionary["title"] = subject
    dictionary["body"] = description
    dictionary["labels"] = [statusLabel, severityLabel, categoryLabel, releaseNumLabel]
    jsonString = json.dumps(dictionary)

    curl = """curl -i -H 'Authorization: token %s' -d '%s' %s""" %(token, jsonString, githubUrl)
    postRequest(curl)
    return

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

if __name__ == "__main__":
    main(sys.argv)
