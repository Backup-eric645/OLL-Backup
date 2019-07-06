class Restore:
    def __init__(self, **kwargs):
        print("Initiating...", end="")
        self.root = kwargs['root']
        oll = kwargs['oll']
        self.oll = oll
        p = ''
        e6 = 0
        print(" Done.")
        for ep in open(oll).read().split("&"):
            print("Getting byte", hex(e6).lstrip('0x') + " (" + str(e6) + ") of list...", end="")
            p += chr(eval(ep))
            print(" Done.")
            e6 += 1
        print("Evaluating and processing...", end="")
        self.p = eval(p)
        print(" Done.")
    def st(self):
        for zi in self.p:
            print("Copying from values:", zi[0], 'to', os.path.join(self.root, zi[0]), end="")
            open(os.path.join(self.root, zi[0]), 'wb').write(zi[1])
            print(" Done.")
