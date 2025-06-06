# MPesaCallbackResponseCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer name | [optional] 
**mobile_number** | **str** | Customer mobile number | [optional] 
**reference** | **str** | Customer reference | [optional] 

## Example

```python
from jenga_client.models.m_pesa_callback_response_customer import MPesaCallbackResponseCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaCallbackResponseCustomer from a JSON string
m_pesa_callback_response_customer_instance = MPesaCallbackResponseCustomer.from_json(json)
# print the JSON string representation of the object
print(MPesaCallbackResponseCustomer.to_json())

# convert the object into a dict
m_pesa_callback_response_customer_dict = m_pesa_callback_response_customer_instance.to_dict()
# create an instance of MPesaCallbackResponseCustomer from a dict
m_pesa_callback_response_customer_from_dict = MPesaCallbackResponseCustomer.from_dict(m_pesa_callback_response_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


