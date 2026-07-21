from pathlib import Path
log_folder = Path("logs")
for file in log_folder.glob("*.log"):
    print(file)