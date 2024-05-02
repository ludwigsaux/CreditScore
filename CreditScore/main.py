import csv
from CreditScore.exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile

class CreditScoreProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.CreditScoreEvent = {}

    def process_file(self):
        try:
            with open(self.filename, newline='') as csvfile:
                data = csv.reader(csvfile, delimiter=',')
                if not self.filename.lower().endswith('.csv'):
                    ext = self.filename.lower().split('.')[1]
                    raise BadExtensionFile(extension=ext)

                for row in data:
                    try:
                        if len(row) != 3:
                            raise InvalidElementsRow(longueur=len(row))
                    except InvalidElementsRow as e:
                        self.CreditScoreEvent[str(row[:])] = str(e)

                    for elements in row:
                        pass
                print(self.CreditScoreEvent)

        except FileNotFoundError:
            print(f"Le fichier '{self.filename}' n'a pas été trouvé.")

        except BadExtensionFile as e:
            ext = self.filename.lower().split('.')[1]
            print(e)

if __name__ == "__main__":
    processor = CreditScoreProcessor('updateDatabase.csv')
    processor.process_file()