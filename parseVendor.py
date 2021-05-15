import bcrypt
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

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

count = 0
while (count < 40):
    count += 1;
    password = get_random_string(8)
    hashed = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode("utf-8")
    print(count)
    print(hashed)
    cursor = db.cursor()
    cursor.execute("UPDATE Vendor SET password =(%s) WHERE vendor_id=(%s)", (hashed, count))

db.commit()


