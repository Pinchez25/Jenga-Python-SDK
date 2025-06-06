# MPesaStkPushResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**MPesaStkPushResponseDataOrder**](MPesaStkPushResponseDataOrder.md) |  | [optional] 
**invoices** | [**List[MPesaTransactionStatusDataInvoicesInner]**](MPesaTransactionStatusDataInvoicesInner.md) |  | [optional] 

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


