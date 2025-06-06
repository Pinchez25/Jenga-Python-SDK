# MPesaTransactionStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**MPesaTransactionStatusDataOrder**](MPesaTransactionStatusDataOrder.md) |  | [optional] 

## Example

```python
from jenga_client.models.m_pesa_transaction_status_data import MPesaTransactionStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaTransactionStatusData from a JSON string
m_pesa_transaction_status_data_instance = MPesaTransactionStatusData.from_json(json)
# print the JSON string representation of the object
print(MPesaTransactionStatusData.to_json())

# convert the object into a dict
m_pesa_transaction_status_data_dict = m_pesa_transaction_status_data_instance.to_dict()
# create an instance of MPesaTransactionStatusData from a dict
m_pesa_transaction_status_data_from_dict = MPesaTransactionStatusData.from_dict(m_pesa_transaction_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


