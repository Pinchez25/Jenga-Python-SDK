# BillValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **int** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**data** | [**BillValidationResponseData**](BillValidationResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.bill_validation_response import BillValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillValidationResponse from a JSON string
bill_validation_response_instance = BillValidationResponse.from_json(json)
# print the JSON string representation of the object
print(BillValidationResponse.to_json())

# convert the object into a dict
bill_validation_response_dict = bill_validation_response_instance.to_dict()
# create an instance of BillValidationResponse from a dict
bill_validation_response_from_dict = BillValidationResponse.from_dict(bill_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


