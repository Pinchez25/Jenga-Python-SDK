# BillPaymentRequestPayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the person making the payment | 
**account** | **str** | The account number for the payer | 
**reference** | **str** | The reference number for the payer&#39;s transaction | 
**mobile_number** | **str** | The mobile number of the payer | 

## Example

```python
from jenga_client.models.bill_payment_request_payer import BillPaymentRequestPayer

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentRequestPayer from a JSON string
bill_payment_request_payer_instance = BillPaymentRequestPayer.from_json(json)
# print the JSON string representation of the object
print(BillPaymentRequestPayer.to_json())

# convert the object into a dict
bill_payment_request_payer_dict = bill_payment_request_payer_instance.to_dict()
# create an instance of BillPaymentRequestPayer from a dict
bill_payment_request_payer_from_dict = BillPaymentRequestPayer.from_dict(bill_payment_request_payer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


