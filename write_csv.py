import csv
logs = [
    ["date", "level", "message"],
    ["2026-07-21", "INFO", "Login Success"],
    ["2026-07-21", "WAARNING", "Disk usage 80%"],
    ["2026-07-21," "ERROR", "Database connection failed"], 
     ]
with open("output.csv", "w" ,encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(logs)