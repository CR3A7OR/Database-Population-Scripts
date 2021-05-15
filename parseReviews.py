import json
import ast
import mysql.connector
import random
import datetime as dt

db = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="DB password",
  database="DB name"
)

f = open("Reviews.json", "r")
Lines = f.readlines()
 
count = 0
count2 = 0
cursor = db.cursor()
# Strips the newline character
for line in Lines:
    if (count < 31000):
        count += 1
        print(count)
        item = json.loads(line)

        try:
            #Product ID
            product = random.randint(1, 10452)

            #Consumer ID
            consumer = random.randint(1, 11)

            #Title
            tempT = item['summary']
            if (tempT):
                title = tempT
            else:
                title = "Great Product"

            #Body
            tempB = item['reviewText']
            if (tempB):
                body = tempB
            else:
                body = "Amazing Product, really do recommend it to anyone who is interest"

            #Rating
            tempR = item['overall']
            if (tempR):
                tempR = int(tempR)
                if (tempR <= 5):
                    rating = tempR
                else:
                    rating = 3
            else:
                rating = 4

            #Date
            tempD = item['reviewTime']
            if (tempD):
                tempD = tempD.replace(',',"")
                d = dt.datetime.strptime(tempD, "%m %d %Y")
                d = d.date()
                d = d.isoformat()
            else:
                d = "2021-05-01"
            
            cursor.execute("INSERT INTO Review (product_id, consumer_id, title, body, rating, date_created) VALUES (%s,%s,%s,%s,%s,%s)", (product, consumer, title, body, rating, d))

        except:
            print("ERROR AT: " + str(count))
db.commit()

