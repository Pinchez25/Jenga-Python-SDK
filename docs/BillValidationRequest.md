# BillValidationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller_code** | **str** | The code for the biller. This is provided by the service provider. | 
**customer_ref_number** | **str** | The reference number for the customer&#39;s bill. | 
**amount** | **str** | The amount to be validated. | 
**amount_currency** | **str** | The currency of the amount (e.g., KES, USD). | 

## Example

```python
from jenga_client.models.bill_validation_request import BillValidationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillValidationRequest from a JSON string
bill_validation_request_instance = BillValidationRequest.from_json(json)
# print the JSON string representation of the object
print(BillValidationRequest.to_json())

# convert the object into a dict
bill_validation_request_dict = bill_validation_request_instance.to_dict()
# create an instance of BillValidationRequest from a dict
bill_validation_request_from_dict = BillValidationRequest.from_dict(bill_validation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


