import filecmp;
import os;
from pathlib import Path;

src_dir = os.path.dirname(os.path.abspath(__file__))
print("src_dir:     ", src_dir)
build_dir = Path(src_dir).parent
print("build_dir:   ", build_dir)
resources_dir = os.path.join(build_dir, "resources")
print("resources_dir:   ", resources_dir)
logrotate11_File_Path = os.path.join(resources_dir, "logrotate11.conf")
print(logrotate11_File_Path)
logrotate22_File_Path = os.path.join(resources_dir, "logrotate22.conf")
print(logrotate22_File_Path)
print("file contents are equal? ", filecmp.cmp(logrotate11_File_Path, logrotate22_File_Path))
assert filecmp.cmp(logrotate11_File_Path, logrotate22_File_Path) == True


