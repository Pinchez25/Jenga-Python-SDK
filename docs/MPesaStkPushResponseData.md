# MPesaStkPushResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Transaction amount | [optional] 
**charge** | **float** | Service charge | [optional] 
**payment_reference** | **str** | Payment reference | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**order_reference** | **str** | Order reference | [optional] 
**amount_debited** | **float** | Amount debited | [optional] 

## Example

```python
from jenga_client.models.m_pesa_stk_push_response_data import MPesaStkPushResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushResponseData from a JSON string
m_pesa_stk_push_response_data_instance = MPesaStkPushResponseData.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushResponseData.to_json())

# convert the object into a dict
m_pesa_stk_push_response_data_dict = m_pesa_stk_push_response_data_instance.to_dict()
# create an instance of MPesaStkPushResponseData from a dict
m_pesa_stk_push_response_data_from_dict = MPesaStkPushResponseData.from_dict(m_pesa_stk_push_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


