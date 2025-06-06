# MPesaCallbackResponseTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | Transaction date | [optional] 
**reference** | **str** | Transaction reference | [optional] 
**payment_mode** | **str** | Payment mode | [optional] 
**amount** | **float** | Transaction amount | [optional] 
**currency** | **str** | Transaction currency | [optional] 
**service_charge** | **float** | Service charge | [optional] 
**bill_number** | **str** | Bill number | [optional] 
**served_by** | **str** | Service provider | [optional] 
**additional_info** | **str** | Additional information | [optional] 
**order_amount** | **float** | Order amount | [optional] 
**order_currency** | **str** | Order currency | [optional] 
**status** | **str** | Transaction status | [optional] 
**remarks** | **str** | Transaction remarks | [optional] 

## Example

```python
from jenga_client.models.m_pesa_callback_response_transaction import MPesaCallbackResponseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaCallbackResponseTransaction from a JSON string
m_pesa_callback_response_transaction_instance = MPesaCallbackResponseTransaction.from_json(json)
# print the JSON string representation of the object
print(MPesaCallbackResponseTransaction.to_json())

# convert the object into a dict
m_pesa_callback_response_transaction_dict = m_pesa_callback_response_transaction_instance.to_dict()
# create an instance of MPesaCallbackResponseTransaction from a dict
m_pesa_callback_response_transaction_from_dict = MPesaCallbackResponseTransaction.from_dict(m_pesa_callback_response_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


