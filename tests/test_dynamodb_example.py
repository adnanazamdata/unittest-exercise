import sys
sys.path.insert(0, 'C:/Users/DELL/python-unittest-exercise')
import boto3
import unittest
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
from botocore.exceptions import ClientError
from botocore.exceptions import ParamValidationError

model_instance = DynamodBExample()


@mock_dynamodb2
def test_create_dynamo_table(self):
    self.conn = boto3.resource('dynamodb', region_name='us-east-1')

    model_instance.create_movies_table()

    self.table = self.conn.Table('Movies')

    self.assertIn('Movies', self.table.name)


@mock_dynamodb2
def test_add_dynamo_record_table(self):
    
    assertEqual(1,1)

@mock_dynamodb2
def test_add_dynamo_record_table_failure(self):
    self.conn = boto3.resource('dynamodb', region_name='us-east-1')

    with self.assertRaises(ParamValidationError) as exc:
        model_instance.add_dynamo_record('Movies', "The Big New Movie")


if __name__ == '__main__':
    unittest.main()
