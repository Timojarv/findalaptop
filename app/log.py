LEVEL_DEBUG=0
LEVEL_INFO=1
LEVEL_WARNING=2
LEVEL_ERROR=3

PREFIX = ['[DEBUG]', '[INFO]', '[WARNING]', '[ERROR]']

class Logger():
    def __init__(self):
        self.debug = LEVEL_DEBUG
        self.info = LEVEL_INFO
        self.warning = LEVEL_WARNING
        self.error = LEVEL_ERROR

    def setLevel(self, level):
        self.level = level

    def log(self, msg, level=None):
        if level == None:
            level = self.level
        print PREFIX[level] + " " + msg
