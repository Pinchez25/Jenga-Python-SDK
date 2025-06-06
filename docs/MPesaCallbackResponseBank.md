# MPesaCallbackResponseBank


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Bank reference | [optional] 
**transaction_type** | **str** | Transaction type | [optional] 
**account** | **str** | Account number | [optional] 

## Example

```python
from jenga_client.models.m_pesa_callback_response_bank import MPesaCallbackResponseBank

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaCallbackResponseBank from a JSON string
m_pesa_callback_response_bank_instance = MPesaCallbackResponseBank.from_json(json)
# print the JSON string representation of the object
print(MPesaCallbackResponseBank.to_json())

# convert the object into a dict
m_pesa_callback_response_bank_dict = m_pesa_callback_response_bank_instance.to_dict()
# create an instance of MPesaCallbackResponseBank from a dict
m_pesa_callback_response_bank_from_dict = MPesaCallbackResponseBank.from_dict(m_pesa_callback_response_bank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


