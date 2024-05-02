class NegativeId(Exception):
    def __init__(self, person_id, message=""):
        super().__init__("Invalid Id : " + str(person_id))
    pass
