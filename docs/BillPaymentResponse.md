# BillPaymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Overall status of the response | [optional] 
**code** | **int** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**reference** | **str** | Bill reference number | [optional] 
**data** | [**BillPaymentResponseData**](BillPaymentResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.bill_payment_response import BillPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentResponse from a JSON string
bill_payment_response_instance = BillPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(BillPaymentResponse.to_json())

# convert the object into a dict
bill_payment_response_dict = bill_payment_response_instance.to_dict()
# create an instance of BillPaymentResponse from a dict
bill_payment_response_from_dict = BillPaymentResponse.from_dict(bill_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


