# MPesaStkPushRequestOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_reference** | **str** | Order reference, should be unique per order | 
**order_amount** | **float** | Original order amount | 
**order_currency** | **str** | Currency of the order | 
**source** | **str** | Source of the order | 
**country_code** | **str** | Source country code (alpha-2) | 
**description** | **str** | Description of the order | 

## Example

```python
from jenga_client.models.m_pesa_stk_push_request_order import MPesaStkPushRequestOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushRequestOrder from a JSON string
m_pesa_stk_push_request_order_instance = MPesaStkPushRequestOrder.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushRequestOrder.to_json())

# convert the object into a dict
m_pesa_stk_push_request_order_dict = m_pesa_stk_push_request_order_instance.to_dict()
# create an instance of MPesaStkPushRequestOrder from a dict
m_pesa_stk_push_request_order_from_dict = MPesaStkPushRequestOrder.from_dict(m_pesa_stk_push_request_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


