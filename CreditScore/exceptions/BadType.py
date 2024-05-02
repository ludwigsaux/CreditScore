class BadType(Exception):
    def __init__(self, person_id, message=""):
        super().__init__("Invalid type : " + str(person_id))
    pass
