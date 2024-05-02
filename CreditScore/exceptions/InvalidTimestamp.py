class InvalidTimestamp(Exception):
    def __init__(self, timestamp, message=""):
        super().__init__("Invalid Timestamp : " + str(timestamp))
    pass
