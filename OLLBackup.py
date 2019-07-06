import os
__all__ = []
class BackupModeError(Exception):
    pass
from Assets.Backup import Backup
from Assets.Restore import Restore
import sys
try:
    if sys.argv[1].lower() == "backup":
        Backup(backupType=sys.argv[2], root=sys.argv[3], oll=sys.argv[4]).st()
    elif sys.argv[1].lower() == "restore":
        Restore(root=sys.argv[2], oll=sys.argv[3]).st()
    elif sys.argv[1].lower() == "-h" or '/?' or '?' or "help" or "--help" or "hlp" or "--hlp":
        print("""OLL Backup
Arg Commands:
BACKUP - backup with arg 1 as type (bin, hex, oct, or dec), arg 2 as backup root, and arg 3 as oll
RESTORE - restore with arg 1 as backup root, and arg 2 as oll
Commands are case-insensitive.""")
    else:
        print("Unrecognized command", *sys.argv[1:])
except IndexError:
    print("""OLL Backup
Arg Commands:
BACKUP - backup with arg 1 as type (bin, hex, oct, or dec), arg 2 as backup root, and arg 3 as oll
RESTORE - restore with arg 1 as backup root, and arg 2 as oll
Commands are case-insensitive.""")
except BackupModeError:
    print("Backup mode not supported")
