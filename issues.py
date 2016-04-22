import os
import sys
import csv
import json
import urllib
from config import *
import time

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

def createIssue(row, projectName):
    dictionary = {}
    project = projectName
    experimentName = row[column["Experiment name"]]
    feature = row[column["Feature"]]
    testStepNum = row[column["Test Step No"]]
    testStepNum = testStepNum.zfill(2)
    subject = "QA_%s_%s" %(experimentName, feature)

    explink = urllib.quote(experimentName)
    featureLink = urllib.quote(feature)
    link =  "https://github.com/%s/%s/blob/master/test-cases/integration_test-cases/%s/%s_%s_%s.org" %(organization, project, explink, explink, testStepNum, featureLink) 
    description = row[column["Description"]] + "\n Test Step Link:\n%s" %(link)

    statusLabel = "Status: " + row[column["Status"]]
    severityLabel = "Severity: " + row[column["Severity"]]
    categoryLabel = "Category: " + row[column["Category"]]
#assignedByLabel = "Assigned by: " + row[column["Assigned by"]]
    releaseNumLabel = "Release Number: " + row[column["Release Number"]]
#   dateLabel = "Start Date: " + row[column["Start date"]]
    developedByLabel = "Developed By: " + row[column["Developed By"]]

    dictionary["title"] = subject
    dictionary["body"] = description
    dictionary["labels"] = [statusLabel, severityLabel, categoryLabel, releaseNumLabel, developedByLabel]
    jsonString = json.dumps(dictionary)

    curl = """curl -g -i -H 'Authorization: token %s' -d '%s' %s""" %(token, jsonString, githubUrl)
    postRequest(curl)
    return

def main(args):
    filePointer = open(args[1], 'r')
    basename = os.path.basename(args[1])
    projectName = basename.rstrip(".csv")
    reader = csv.reader(filePointer, delimiter=',')
    header = reader.next()
    defineTitle(header)
#    printIssue(reader)
    rowIndex = 1
    row = reader.next()
    while row:
        createIssue(row, projectName)
	row = reader.next()
	rowIndex+=1
	if rowIndex >= 34:
	    time.sleep(10)
	    rowIndex = 1

    filePointer.close()
    return

if __name__ == "__main__":
    main(sys.argv)
