import openpyxl
import psycopg2

DATABASE_URL = 'postgres://bfcikbkerzsrki:4dd97e251f6d60774b6d6a480328992196ff4c6efed1e5f3e4ea806b6882678f@ec2-54-220-170-192.eu-west-1.compute.amazonaws.com:5432/d8hqi7m20195lj'

with psycopg2.connect(DATABASE_URL, sslmode='require') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

file = openpyxl.load_workbook('Книга.xlsx')
sh = file[file.sheetnames[0]]
for row in rows:
    sh.append(row)
file.save('Книга.xlsx')
