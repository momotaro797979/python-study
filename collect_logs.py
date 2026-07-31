from pathlib import Path
def collect_logs():
    log_folder = Path("logs")
    all_logs = []
    for file in log_folder.glob("*.log"):
        count = 0
        try:
            with open(file,"r",encoding="utf-8")as f:
                for line in f:
                    if line.strip():
                        all_logs.append(line.strip())
                        count += 1
            print(f"{file.name} : {count}件")  
        except OSError as error:
                print(f"{file.name} : を読み込めませんでした")
                print(error)
    print()
    print("ログ件数",len(all_logs))
    return all_logs




logs = collect_logs()
print(logs)