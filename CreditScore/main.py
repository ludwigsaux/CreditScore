import csv
from CreditScore.exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile

CreditScoreEvent = {}
filename = 'updateDatabase.xlsx'

try :
    with open(filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        '''try :
            if not filename.lower().endswith('.csv'):
                ext= filename.lower().split('.')[1]
                raise BadExtensionFile(extension=ext)
        except BadExtensionFile as e:
            print(e)'''
        for row in data:
            try:
                if len(row) != 3:
                    raise InvalidElementsRow(longueur=len(row))
            except InvalidElementsRow as e:
                CreditScoreEvent[str(row[:])] = str(e)

            for elements in row:
                pass
        print(CreditScoreEvent)

except ValueError:
    ext = filename.lower().split('.')[1]
    raise BadExtensionFile(extension=ext)




# CSV
    # combien d'element dans la ligne ?

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




