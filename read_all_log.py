from pathlib import Path
log_folder = Path("logs")
for file in log_folder.glob("*.log"):
    print(f"===={file.name}====")
    with open (file,"r",encoding="utf-8")as f:
        print(f.read())