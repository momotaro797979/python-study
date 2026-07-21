import json
logs = [
    {
        "date":"2026-07-21",
        "level":"INFO",
        "message":"Login Success"
    },
    {
        "date":"2026-07-21",
        "level":"WARNING",
        "message":"Disk usage 80%"
    },
    {
        "date":"2026-07-21",
        "level":"ERROR",
        "messsage":"DAtabase connection failed"
    }
]
with open("output.json","w",encoding="utf-8") as file:
    json.dump(logs,file,ensure_ascii=False,indent=4)