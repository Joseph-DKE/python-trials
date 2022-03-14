import mysql.connector

# Configure database
connection = mysql.connector.MySQLConnection(
  host     = "",
  user     = "",
  passwd   = "",
  db       = "",
  ssl_ca   = ""
)
db = connection.cursor()
connection.autocommit = True

db.execute("SELECT * FROM students")
rows = db.fetchall()

print(rows)