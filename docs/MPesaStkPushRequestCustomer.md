# MPesaStkPushRequestCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Customer&#39;s name | 
**email** | **str** | Customer&#39;s email | 
**phone_number** | **str** | Customer&#39;s phone number | 
**identity_number** | **str** | Customer&#39;s identity number | 
**first_address** | **str** | Customer&#39;s first address | [optional] 
**second_address** | **str** | Customer&#39;s second address | [optional] 

## Example

```python
from jenga_client.models.m_pesa_stk_push_request_customer import MPesaStkPushRequestCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaStkPushRequestCustomer from a JSON string
m_pesa_stk_push_request_customer_instance = MPesaStkPushRequestCustomer.from_json(json)
# print the JSON string representation of the object
print(MPesaStkPushRequestCustomer.to_json())

# convert the object into a dict
m_pesa_stk_push_request_customer_dict = m_pesa_stk_push_request_customer_instance.to_dict()
# create an instance of MPesaStkPushRequestCustomer from a dict
m_pesa_stk_push_request_customer_from_dict = MPesaStkPushRequestCustomer.from_dict(m_pesa_stk_push_request_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


