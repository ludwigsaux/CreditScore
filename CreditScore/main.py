import csv
#from exceptions.InvalidElementsRow import InvalidElementsRow
#from exceptions.BadExtensionFile import BadExtensionFile
#from exceptions.NegativeId import NegativeId
#from exceptions.InvalidTimestamp import InvalidTimestamp
from datetime import datetime

class CreditScoreProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.CreditScoreEvent = {}

    def process_file(self):
        self.validate_file_extension()
        with open(self.filename, newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            next(data)  # Skip header row
            for row in data:
                self.execute_line(row)
        print(self.CreditScoreEvent)

    def validate_file_extension(self):
        try:
            if not self.filename.lower().endswith('.csv'):
                ext = self.filename.lower().split('.')[1]
                raise BadExtensionFile(extension=ext)
        except FileNotFoundError:
            print(f"Le fichier '{self.filename}' n'a pas été trouvé.")

    def execute_line(self, row):
        try:
            self.validate_row_length(row)
            person_id = self.validate_person_id(row[0])
            timestamp = self.validate_timestamp(row[1])
            credit_score = self.validate_credit_score(row[2])
            # TODO: Process valid data (person_id, timestamp, credit_score)
        except (InvalidElementsRow, NegativeId, InvalidTimestamp, ValueError) as e:
            self.CreditScoreEvent[str(row[:])] = str(e)

    def validate_row_length(self, row):
        if len(row) != 3:
            raise InvalidElementsRow(longueur=len(row))

    def validate_person_id(self, person_id_str):
        try:
            person_id = int(person_id_str)
            if person_id <= 0:
                raise NegativeId(person_id)
            return person_id
        except ValueError:
            raise InvalidElementsRow(f"PersonId '{person_id_str}' n'est pas un entier valide")

    def validate_timestamp(self, timestamp_str):
        if not self.is_valid_timestamp(timestamp_str):
            raise InvalidTimestamp(timestamp_str)
        return timestamp_str

    def validate_credit_score(self, credit_score_str):
        if credit_score_str:
            try:
                credit_score = int(credit_score_str)
                if not 300 <= credit_score <= 850:
                    raise ValueError(f"CreditScore must be between 300 and 850: {credit_score}")
                return credit_score
            except ValueError:
                raise InvalidElementsRow(f"CreditScore '{credit_score_str}' n'est pas un entier valide")
        else:
            return None

    def is_valid_timestamp(self, timestamp):
        try:
            datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    processor = CreditScoreProcessor('updateDatabase.csv')
    processor.process_file()