# MPesaStkPushRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**MPesaStkPushRequestOrder**](MPesaStkPushRequestOrder.md) |  | 
**customer** | [**MPesaStkPushRequestCustomer**](MPesaStkPushRequestCustomer.md) |  | 
**payment** | [**MPesaStkPushRequestPayment**](MPesaStkPushRequestPayment.md) |  | 

## Example

```python
from jenga_client.models.m_pesa_stk_push_request import MPesaStkPushRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushRequest from a JSON string
m_pesa_stk_push_request_instance = MPesaStkPushRequest.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushRequest.to_json())

# convert the object into a dict
m_pesa_stk_push_request_dict = m_pesa_stk_push_request_instance.to_dict()
# create an instance of MPesaStkPushRequest from a dict
m_pesa_stk_push_request_from_dict = MPesaStkPushRequest.from_dict(m_pesa_stk_push_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


