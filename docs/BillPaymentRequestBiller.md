# BillPaymentRequestBiller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller_code** | **str** | The unique code for the biller | 
**country_code** | **str** | The country code of the biller | 

## Example

```python
from jenga_client.models.bill_payment_request_biller import BillPaymentRequestBiller

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentRequestBiller from a JSON string
bill_payment_request_biller_instance = BillPaymentRequestBiller.from_json(json)
# print the JSON string representation of the object
print(BillPaymentRequestBiller.to_json())

# convert the object into a dict
bill_payment_request_biller_dict = bill_payment_request_biller_instance.to_dict()
# create an instance of BillPaymentRequestBiller from a dict
bill_payment_request_biller_from_dict = BillPaymentRequestBiller.from_dict(bill_payment_request_biller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


