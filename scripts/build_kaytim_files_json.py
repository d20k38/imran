import json,sys
from datetime import datetime
from zoneinfo import ZoneInfo

with open(sys.argv[1],encoding="utf-8") as f:
    data=json.load(f)

now=datetime.now(ZoneInfo("Europe/Istanbul"))
out={
    "generated_at":now.isoformat(timespec="seconds"),
    "timezone":"Europe/Istanbul",
    "site":"kaytim.neocities.org",
    "files":data.get("files",[])
}
with open(sys.argv[2],"w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=2)
    f.write("\n")
