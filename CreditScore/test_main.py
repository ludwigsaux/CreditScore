import unittest
from unittest.mock import patch, mock_open
from exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile
import io
from CreditScore.CreditScore import CreditScoreProcessor


# test commit
class TestCreditScoreEvent(unittest.TestCase):
    def test_all_good(self):
        processor = CreditScoreProcessor('updateDatabase.csv')
        processor.process_file()
        self.assertEqual(processor.CreditScoreEvent, {})
        
    @patch('builtins.open', new_callable=mock_open, read_data='PersonId,TimeStamp,CreditScore')
    def test_valid_csv(self, mock_file):
        processor = CreditScoreProcessor('updateDatabase.csv')
        processor.process_file()
        expected_output = {"['4;05-05-2024 09:32:20', '720']": 'Invalid number of elements in row : 2'}
        self.assertEqual(processor.CreditScoreEvent, expected_output)

if __name__ == '__main__':
    unittest.main()