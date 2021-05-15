import random
import string
import ast
import mysql.connector

db = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="DB password",
  database="DB name"
)

count = 0
cursor = db.cursor()
while (count < 1):
    count += 1;
    cursor.execute("SELECT title FROM Product WHERE product_id = %s", (count,))
    tags = cursor.fetchone()
      
    if (tags):
        print(count)
        test1 = tags[0]
        words = test1.split()
        test3 = words[:20]
        test = ' '.join(test3)
        test = test.replace("and", "")
        test = test.replace("of", "")
        test = test.replace(' ',', ')
        test = test.replace(',,', ', ')
        test = test.replace(';,', ', ')
        cursor.execute("UPDATE Product SET tags = %s WHERE product_id= %s", (test, count))
    else:
        print(tags)


db.commit()
