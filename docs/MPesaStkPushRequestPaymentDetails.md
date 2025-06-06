# MPesaStkPushRequestPaymentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msisdn** | **str** | Number to push the STK | 
**payment_amount** | **float** | Amount to pay on the request | 

## Example

```python
from jenga_client.models.m_pesa_stk_push_request_payment_details import MPesaStkPushRequestPaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushRequestPaymentDetails from a JSON string
m_pesa_stk_push_request_payment_details_instance = MPesaStkPushRequestPaymentDetails.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushRequestPaymentDetails.to_json())

# convert the object into a dict
m_pesa_stk_push_request_payment_details_dict = m_pesa_stk_push_request_payment_details_instance.to_dict()
# create an instance of MPesaStkPushRequestPaymentDetails from a dict
m_pesa_stk_push_request_payment_details_from_dict = MPesaStkPushRequestPaymentDetails.from_dict(m_pesa_stk_push_request_payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


