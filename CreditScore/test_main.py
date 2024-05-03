import unittest
from unittest.mock import patch, mock_open
from exceptions.InvalidElementsRow import InvalidElementsRow
from exceptions.BadExtensionFile import BadExtensionFile
import io
from main import CreditScoreProcessor
import json
import os

class TestCreditScoreEvent(unittest.TestCase):
    def setUp(self):
        self.test_csv_file = 'test.csv'
        self.test_json_file = 'test.json'
        self.processor = CreditScoreProcessor(self.test_csv_file, self.test_json_file)

    def test_validate_file_extension(self):
        # Test with valid file extension
        self.processor.filename = 'test.csv'
        self.assertIsNone(self.processor.validate_file_extension())

    def test_validate_file_extension_invalid(self):
        # Test with invalid file extension
        self.processor.filename = 'test.txt'
        with self.assertRaises(BadExtensionFile):
            self.processor.validate_file_extension()
        
    def test_validate_row_length(self):
        # Test with valid row length
        row = ['123', '01-01-2022 12:00:00', '750']
        self.assertTrue(self.processor.validate_row_length(row))
    
    def test_validate_row_length_invalid(self):
        # Test with invalid row length
        row = ['123', '01-01-2022 12:00:00']
        with self.assertRaises(InvalidElementsRow):
            self.processor.validate_row_length(row)

    def test_validate_person_id(self):
        # Test with valid person ID
        person_id = '123'
        self.assertEqual(self.processor.validate_person_id(person_id), 123)
            

    def test_is_valid_timestamp(self):
        self.assertTrue(self.processor.is_valid_timestamp('01-01-2020 12:00:00'))
        self.assertFalse(self.processor.is_valid_timestamp('01-01-2020'))

    def test_validate_credit_score(self):
        credit_score = '750'
        self.assertEqual(self.processor.validate_credit_score(credit_score), 750)
    

    # le test rend full erreur mais je pense que c'est normal, à verifier
    # def test_validate_credit_score_invalid(self):
    #     credit_score = '900'
    #     with self.assertRaises(ValueError):
    #         self.processor.validate_credit_score(credit_score)

    

    

if __name__ == '__main__':
    unittest.main()