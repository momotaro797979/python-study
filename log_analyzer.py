logs = [
    "ERROR Login failed",
    "INFO Login succes",
    "WARNING Disk usage",
    "ERROR Timeout"
]
error_count = 0
warning_count = 0
info_count = 0
for log in logs:
    if "ERROR" in log:
        error_count += 1
    elif "WARNING" in log:
        warning_count += 1
    elif "INFO" in log:
        info_count += 1

print(f"ERROR:{error_count}")
print(f"WARNING:{warning_count}")
print(f"INFO:{info_count}")