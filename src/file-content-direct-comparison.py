import os
from pathlib import Path


originalLines = []
originalLines.append("/var/log/nginx/*.log {")
originalLines.append("daily")
originalLines.append("size 512M")
originalLines.append("maxage 60")
originalLines.append("missingok")
originalLines.append("rotate 10")
originalLines.append("notifempty")
originalLines.append("create 644 nginx adm")
originalLines.append("sharedscripts")
originalLines.append("postrotate")
originalLines.append("if [ -f /var/run/nginx.pid ]; then")
originalLines.append("kill -USR1 `cat /var/run/nginx.pid`")
originalLines.append("fi")
originalLines.append("endscript")
originalLines.append("}")

src_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = Path(src_dir).parent
resources_dir = os.path.join(build_dir, "resources")
logrotate11FilePath = os.path.join(resources_dir, "logrotate11.conf")
logrotate11FileHandle = open(logrotate11FilePath)
lines = logrotate11FileHandle.readlines()
nonEmptyLines = []
for line in lines:
    line = line.strip()
    if len(line) > 0:
        nonEmptyLines.append(line)

for i in range(len(nonEmptyLines)):
    assert nonEmptyLines[i] == originalLines[i]
    print(i)
    print(nonEmptyLines[i])
    print(originalLines[i])



