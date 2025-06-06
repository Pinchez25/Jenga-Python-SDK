# BillPaymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller** | [**BillPaymentRequestBiller**](BillPaymentRequestBiller.md) |  | 
**bill** | [**BillPaymentRequestBill**](BillPaymentRequestBill.md) |  | 
**payer** | [**BillPaymentRequestPayer**](BillPaymentRequestPayer.md) |  | 
**partner_id** | **str** | The ID of the partner initiating the payment | 
**remarks** | **str** | Additional remarks about the payment | [optional] 

## Example

```python
from jenga_client.models.bill_payment_request import BillPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillPaymentRequest from a JSON string
bill_payment_request_instance = BillPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(BillPaymentRequest.to_json())

# convert the object into a dict
bill_payment_request_dict = bill_payment_request_instance.to_dict()
# create an instance of BillPaymentRequest from a dict
bill_payment_request_from_dict = BillPaymentRequest.from_dict(bill_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


