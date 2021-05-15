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

f = open("meta_Appliances.json", "r")
Lines = f.readlines()
 
count = 0
count2 = 0
# Strips the newline character
for line in Lines:
    if (count < 30445): 
        count += 1
        print(count)
        x = '{}'.format(line)
        x = ast.literal_eval(x)
        data = json.dumps(x)
        item = json.loads(data)
        try:
            #Format a description
            temp = item['description']
            desc = json.dumps(temp)
            desc = desc[2:]
            desc = desc[:len(desc)-2]
            if (desc == ""):
                desc = "N/A"
            
            #Collect first image from list
            tempI = item['image']
            if (tempI):
                image = tempI[0]
            else:
                image = "N/A"

            #Format Category
            tempC = item['category']
            if (tempC):
                category = tempC[1]
            else:
                category = "N/A"

            #Generate a quantity
            quantity = random.randint(1, 75)

            #Pick a random a store_id
            store = random.randint(1, 50)

            #Price
            tempP = item['price']
            if (tempP):
                first_char = tempP[0]
                if (first_char == '$'):
                    tempP = tempP[1:]
                    tempP = tempP.replace(',',"")
                    price = float(tempP)
                else:
                    price = random.randint(3, 100)
            else:
                price = random.randint(3, 100)

            #Date
            tempD = item['date']
            if (tempD):
                tempD = tempD.replace(',',"")
                d = dt.datetime.strptime(tempD, "%B %d %Y")
                d = d.date()
                d = d.isoformat()
            else:
                d = "2021-05-01"

            if (desc != "N/A") and (image != "N/A") and (category != "N/A"):
                count2 += 1
                cursor = db.cursor()
                cursor.execute("INSERT INTO Product (product_id, store_id, title, description, image, category, tags, quantity, price, date_created, available) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (count2, store, item['title'], desc, image, category, "{}", quantity, price, d, 1))
        except:
            print("ERROR: at" + str(count))
    else:
        break

db.commit()

