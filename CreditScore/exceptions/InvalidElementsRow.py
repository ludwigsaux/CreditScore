class InvalidElementsRow(Exception):
    def __init__(self, longueur, message=""):
        super().__init__("Invalid number of elements in row : " + str(longueur))
    pass
