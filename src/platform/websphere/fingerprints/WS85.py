from cprint import FingerPrint


class FPrint(FingerPrint):

    def __init__(self):
        self.platform = 'websphere'
        self.version = 'Any'
        self.title = WSINTERFACES.CON
        self.uri = '/'
        self.port = 9044
        self.hash = None
