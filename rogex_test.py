import re 
log ="2026-08-03 08:15:00 ERROR Login Failed"
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)"
result = re.search(pattern, log)
if result:
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    print(result.group(4))