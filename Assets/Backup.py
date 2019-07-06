from FolderTree import FolderTree
class Backup:
    def __init__(self, **kwargs):
        try:
            self.stream = open(kwargs['oll'], 'w')
        except FileNotFoundError:
            self.stream = open(kwargs['oll'], 'w+')
        files = FolderTree(kwargs['root'])
        mode = kwargs['backupType']
        t = []
        if mode == "dec":
            for mk in str(files):
                t.append(str(ord(mk)))
        elif mode == "hex":
            for mk in str(files):
                t.append(hex(ord(mk)))
        elif mode == "oct":
            for mk in str(files):
                t.append(oct(ord(mk)))
        elif mode == "bin":
            for mk in str(files):
                t.append(bin(ord(mk)))
        else:
            raise BackupModeError("Backup mode not supported")
        self.lm = t
    def st(self):
        self.stream.write('&'.join(self.lm))
