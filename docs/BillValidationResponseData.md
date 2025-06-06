# BillValidationResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Bill amount | [optional] 
**customer_ref_number** | **str** | Bill identifier | [optional] 
**name** | **str** | Bill name | [optional] 
**bill_status** | **str** | Bill status | [optional] 
**message** | **str** | Bill query response message | [optional] 
**created_on** | **str** | Bill create date on third party system | [optional] 
**amount_currency** | **str** | Bill amount currency | [optional] 
**status** | **bool** | Bill status | [optional] 

## Example

```python
from jenga_client.models.bill_validation_response_data import BillValidationResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BillValidationResponseData from a JSON string
bill_validation_response_data_instance = BillValidationResponseData.from_json(json)
# print the JSON string representation of the object
print(BillValidationResponseData.to_json())

# convert the object into a dict
bill_validation_response_data_dict = bill_validation_response_data_instance.to_dict()
# create an instance of BillValidationResponseData from a dict
bill_validation_response_data_from_dict = BillValidationResponseData.from_dict(bill_validation_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


