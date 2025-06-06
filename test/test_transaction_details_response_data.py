# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jenga_client.models.transaction_details_response_data import TransactionDetailsResponseData

class TestTransactionDetailsResponseData(unittest.TestCase):
    """TransactionDetailsResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionDetailsResponseData:
        """Test TransactionDetailsResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionDetailsResponseData`
        """
        model = TransactionDetailsResponseData()
        if include_optional:
            return TransactionDetailsResponseData(
                transaction_id = 'TR123456789',
                amount = 1000.0,
                currency = 'KES',
                status = 'SUCCESS',
                state_code = 2,
                var_date = '2024-02-20T10:00:00Z'
            )
        else:
            return TransactionDetailsResponseData(
        )
        """

    def testTransactionDetailsResponseData(self):
        """Test TransactionDetailsResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
