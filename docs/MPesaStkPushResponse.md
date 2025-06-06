# MPesaStkPushResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **str** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**data** | [**MPesaStkPushResponseData**](MPesaStkPushResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.m_pesa_stk_push_response import MPesaStkPushResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushResponse from a JSON string
m_pesa_stk_push_response_instance = MPesaStkPushResponse.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushResponse.to_json())

# convert the object into a dict
m_pesa_stk_push_response_dict = m_pesa_stk_push_response_instance.to_dict()
# create an instance of MPesaStkPushResponse from a dict
m_pesa_stk_push_response_from_dict = MPesaStkPushResponse.from_dict(m_pesa_stk_push_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


