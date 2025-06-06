# MPesaStkPushRequestPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_reference** | **str** | Payment reference, should be unique per request | 
**payment_currency** | **str** | Currency of the payment | 
**channel** | **str** | Channel of the payment | 
**service** | **str** | Payment service | 
**provider** | **str** | Payment provider | 
**callback_url** | **str** | Callback URL for transaction status | 
**details** | [**MPesaStkPushRequestPaymentDetails**](MPesaStkPushRequestPaymentDetails.md) |  | 

## Example

```python
from jenga_client.models.m_pesa_stk_push_request_payment import MPesaStkPushRequestPayment

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushRequestPayment from a JSON string
m_pesa_stk_push_request_payment_instance = MPesaStkPushRequestPayment.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushRequestPayment.to_json())

# convert the object into a dict
m_pesa_stk_push_request_payment_dict = m_pesa_stk_push_request_payment_instance.to_dict()
# create an instance of MPesaStkPushRequestPayment from a dict
m_pesa_stk_push_request_payment_from_dict = MPesaStkPushRequestPayment.from_dict(m_pesa_stk_push_request_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


