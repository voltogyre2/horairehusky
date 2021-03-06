import json
import os

with open(os.path.dirname(os.path.abspath(__file__))+'/outputpretty.json', 'r') as fp:
    obj = json.load(fp)
fp.close
file = open(os.path.dirname(os.path.abspath(__file__)) + "/NoviceB1.txt","w")
file.write( "************************************************************\n")
file.write( "                        Novice B1 Majeur\n")
file.write( "************************************************************\n")
for event in obj:
    for teams in event["TeamList"]:
        if  teams["Name"].encode('utf-8') == "Novice B1 Majeur" :
            file.write( "=============================\n")
            file.write( event["Title"].encode('utf-8') + "\n")
            file.write( event['Date'].encode('utf-8') + "\n")
            file.write( event['StartTime'].encode('utf-8') + " - " + event['EndTime'].encode('utf-8') + " ( " +  event['Duration'].encode('utf-8') + " )" + "\n")
            file.write( event['SportCenterAbr'].encode('utf-8') + " - " + event['SportCenterName'].encode('utf-8') + "\n")
            for teams in event["TeamList"]:
                file.write( "    " + teams["Name"].encode('utf-8') + "\n")
file.close
file = open(os.path.dirname(os.path.abspath(__file__)) + "/PeeweeA1.txt","w")
file.write( "************************************************************" + "\n")
file.write( "                        Peewee A1" + "\n")
file.write( "************************************************************" + "\n")
for event in obj:
    for teams in event["TeamList"]:
        if  teams["Name"].encode('utf-8') == "Peewee A1":
            file.write( "=============================" + "\n")
            file.write( event["Title"].encode('utf-8') + "\n")
            file.write( event['Date'].encode('utf-8') + "\n")
            file.write( event['StartTime'].encode('utf-8') + " - " + event['EndTime'].encode('utf-8') + " ( " +  event['Duration'].encode('utf-8') + " )" + "\n")
            file.write( event['SportCenterAbr'].encode('utf-8') + " - " + event['SportCenterName'].encode('utf-8') + "\n")
            for teams in event["TeamList"]:
                file.write( "    " + teams["Name"].encode('utf-8') + "\n")

file.close

file = open(os.path.dirname(os.path.abspath(__file__)) + "/Dispo.txt","w")
file.write( "************************************************************" + "\n")
file.write( "                        Glace Dispo" + "\n")
file.write( "************************************************************" + "\n")
for event in obj:
        if  event["Description"].encode('utf-8') == "Glace disponible":
            file.write( "=============================" + "\n")
            file.write( event["Title"].encode('utf-8') + "\n")
            file.write( event['Date'].encode('utf-8') + "\n")
            file.write( event['StartTime'].encode('utf-8') + " - " + event['EndTime'].encode('utf-8') + " ( " +  event['Duration'].encode('utf-8') + " )" + "\n")
            file.write( event['SportCenterAbr'].encode('utf-8') + " - " + event['SportCenterName'].encode('utf-8') + "\n")
            for teams in event["TeamList"]:
                file.write( "    " + teams["Name"].encode('utf-8') + "\n")

file.close
