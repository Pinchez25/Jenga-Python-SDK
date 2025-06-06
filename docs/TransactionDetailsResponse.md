# TransactionDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **str** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**data** | [**TransactionDetailsResponseData**](TransactionDetailsResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.transaction_details_response import TransactionDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDetailsResponse from a JSON string
transaction_details_response_instance = TransactionDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(TransactionDetailsResponse.to_json())

# convert the object into a dict
transaction_details_response_dict = transaction_details_response_instance.to_dict()
# create an instance of TransactionDetailsResponse from a dict
transaction_details_response_from_dict = TransactionDetailsResponse.from_dict(transaction_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


