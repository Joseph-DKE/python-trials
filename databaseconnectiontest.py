import mysql.connector

# Configure database
connection = mysql.connector.MySQLConnection(
  host     = "h60rz6g05y9j.us-east-4.psdb.cloud",
  user     = "99iacl0gsbgk",
  passwd   = "pscale_pw_4aWTdl3CDZLquMMGOmgMefNPw1A5PcIm94H6otZY9JU",
  db       = "thisonepass",
  ssl_ca   = "/etc/ssl/certs/ca-certificates.crt"
)
db = connection.cursor()
connection.autocommit = True

db.execute("SELECT * FROM students")
rows = db.fetchall()

print(rows)