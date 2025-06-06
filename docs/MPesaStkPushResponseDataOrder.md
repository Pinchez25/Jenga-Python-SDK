# MPesaStkPushResponseDataOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_amount** | **float** | Request amount | [optional] 
**amount_paid** | **float** | Amount paid by customer including service charge | [optional] 
**order_reference** | **str** | Order Reference | [optional] 
**order_status** | **str** | Status of an order (Paid, Pending, Expired) | [optional] 
**created_on** | **float** | Creation date of the order in EPOC time | [optional] 

## Example

```python
from jenga_client.models.m_pesa_stk_push_response_data_order import MPesaStkPushResponseDataOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushResponseDataOrder from a JSON string
m_pesa_stk_push_response_data_order_instance = MPesaStkPushResponseDataOrder.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushResponseDataOrder.to_json())

# convert the object into a dict
m_pesa_stk_push_response_data_order_dict = m_pesa_stk_push_response_data_order_instance.to_dict()
# create an instance of MPesaStkPushResponseDataOrder from a dict
m_pesa_stk_push_response_data_order_from_dict = MPesaStkPushResponseDataOrder.from_dict(m_pesa_stk_push_response_data_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


