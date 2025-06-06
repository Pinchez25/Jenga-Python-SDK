# BillPaymentRequestBill


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference number for the bill | 
**amount** | **str** | The amount to be paid | 
**currency** | **str** | The currency for the payment | 

## Example

```python
from jenga_client.models.bill_payment_request_bill import BillPaymentRequestBill

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentRequestBill from a JSON string
bill_payment_request_bill_instance = BillPaymentRequestBill.from_json(json)
# print the JSON string representation of the object
print(BillPaymentRequestBill.to_json())

# convert the object into a dict
bill_payment_request_bill_dict = bill_payment_request_bill_instance.to_dict()
# create an instance of BillPaymentRequestBill from a dict
bill_payment_request_bill_from_dict = BillPaymentRequestBill.from_dict(bill_payment_request_bill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


