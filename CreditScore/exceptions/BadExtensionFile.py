class BadExtensionFile(Exception):
    def __init__(self, extension, message=""):
        super().__init__("Invalid extension : " + extension)
    pass
