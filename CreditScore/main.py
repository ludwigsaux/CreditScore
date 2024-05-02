import csv
from CreditScore.exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile
from exceptions.NegativeId import NegativeId
from datetime import datetime
class CreditScoreProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.CreditScoreEvent = {}

    def execute(self):
        try:
            with open(self.filename, newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                if not self.filename.lower().endswith('.csv'):
                    ext = self.filename.lower().split('.')[1]
                    raise BadExtensionFile(extension=ext)
                next(data)

                for row in data:
                    try:
                        if len(row) != 3:
                            raise InvalidElementsRow(longueur=len(row))

                        person_id = int(row[0])

                        if person_id <= 0:
                            raise NegativeId(person_id)

                        timestamp = row[1]

                        if not self.is_valid_timestamp(timestamp):
                            raise ValueError(f"Invalid timestamp format: {timestamp}")


                        credit_score = row[2]
                        if credit_score:
                            credit_score = int(credit_score)
                            if not 300 <= credit_score <= 850:
                                raise ValueError(f"CreditScore must be between 300 and 850: {credit_score}")
                        else:
                            credit_score = None

                    except InvalidElementsRow as e:
                        self.CreditScoreEvent[str(row[:])] = str(e)

                    except NegativeId as e:
                        self.CreditScoreEvent[str(row[:])] = str(e)

                    for elements in row:
                        pass
                print(self.CreditScoreEvent)

        except FileNotFoundError:
            print(f"Le fichier '{self.filename}' n'a pas été trouvé.")

        except BadExtensionFile as e:
            ext = self.filename.lower().split('.')[1]
            print(e)

    def is_valid_timestamp(self, timestamp):
        try:
            datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    processor = CreditScoreProcessor('updateDatabase.csv')
    processor.process_file()

'''
# CSV
    # combien d'element dans la ligne ?
    # verification fichier existant ou mauvaise extension

# PersonID
    # si existe pas -> pas insert

    # verification type
    # si existe -> remplace si timestamp > actuel
    # verfier positif

# Timestamp
    # verifier type
    # verifier format
    # verification date > date database

# CreditScore
    # verifier type
    # 300 < CreditScore < 850
'''