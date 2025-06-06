# BillPaymentResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Payment transaction ID (returned only if payment is successful) | [optional] 
**status** | **str** | Bill processing status | [optional] 

## Example

```python
from jenga_client.models.bill_payment_response_data import BillPaymentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentResponseData from a JSON string
bill_payment_response_data_instance = BillPaymentResponseData.from_json(json)
# print the JSON string representation of the object
print(BillPaymentResponseData.to_json())

# convert the object into a dict
bill_payment_response_data_dict = bill_payment_response_data_instance.to_dict()
# create an instance of BillPaymentResponseData from a dict
bill_payment_response_data_from_dict = BillPaymentResponseData.from_dict(bill_payment_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


