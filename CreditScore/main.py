import csv
from CreditScore.exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile

CreditScoreEvent = {}
filename = 'updateDatabase.csv'

try :
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        if not filename.lower().endswith('.csv'):
            ext= filename.lower().split('.')[1]
            raise BadExtensionFile(extension=ext)

        for row in data:
            try:
                if len(row) != 3:
                    raise InvalidElementsRow(longueur=len(row))
            except InvalidElementsRow as e:
                CreditScoreEvent[str(row[:])] = str(e)

            for elements in row:
                pass
        print(CreditScoreEvent)

except FileNotFoundError:
    print(f"Le fichier '{filename}' n'a pas été trouvé.")

except BadExtensionFile as e:
    ext = filename.lower().split('.')[1]
    print(e)



'''
# CSV
    # combien d'element dans la ligne ?
    # verification fichier existant ou mauvaise extension

# PersonID
    # si existe pas -> ajout

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



