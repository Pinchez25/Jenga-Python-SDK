# MPesaCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_type** | **str** | Type of callback | [optional] 
**customer** | [**MPesaCallbackResponseCustomer**](MPesaCallbackResponseCustomer.md) |  | [optional] 
**transaction** | [**MPesaCallbackResponseTransaction**](MPesaCallbackResponseTransaction.md) |  | [optional] 
**bank** | [**MPesaCallbackResponseBank**](MPesaCallbackResponseBank.md) |  | [optional] 

## Example

```python
from jenga_client.models.m_pesa_callback_response import MPesaCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaCallbackResponse from a JSON string
m_pesa_callback_response_instance = MPesaCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(MPesaCallbackResponse.to_json())

# convert the object into a dict
m_pesa_callback_response_dict = m_pesa_callback_response_instance.to_dict()
# create an instance of MPesaCallbackResponse from a dict
m_pesa_callback_response_from_dict = MPesaCallbackResponse.from_dict(m_pesa_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


