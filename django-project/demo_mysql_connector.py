import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="shopuser",
  password="shopuser", 
  unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

print(mydb)
