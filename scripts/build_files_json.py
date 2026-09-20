import json,sys
from datetime import datetime,timezone
with open(sys.argv[1],encoding="utf-8") as f:d=json.load(f)
out={"generated_at":datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),"site":"imrann.neocities.org","files":d.get("files",[])}
with open(sys.argv[2],"w",encoding="utf-8") as f: json.dump(out,f,ensure_ascii=False,indent=2);f.write("\n")
