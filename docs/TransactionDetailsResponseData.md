# TransactionDetailsResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction ID | [optional] 
**amount** | **float** | Transaction amount | [optional] 
**currency** | **str** | Transaction currency | [optional] 
**status** | **str** | Transaction status | [optional] 
**state_code** | **int** | State code | [optional] 
**var_date** | **datetime** | Transaction date | [optional] 

## Example

```python
from jenga_client.models.transaction_details_response_data import TransactionDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetailsResponseData from a JSON string
transaction_details_response_data_instance = TransactionDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(TransactionDetailsResponseData.to_json())

# convert the object into a dict
transaction_details_response_data_dict = transaction_details_response_data_instance.to_dict()
# create an instance of TransactionDetailsResponseData from a dict
transaction_details_response_data_from_dict = TransactionDetailsResponseData.from_dict(transaction_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


