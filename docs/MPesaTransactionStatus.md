# MPesaTransactionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Indicates if the request was successful | [optional] 
**code** | **str** | Response code indicating status | [optional] 
**message** | **str** | Description of the response status | [optional] 
**data** | [**MPesaTransactionStatusData**](MPesaTransactionStatusData.md) |  | [optional] 

## Example

```python
from jenga_client.models.m_pesa_transaction_status import MPesaTransactionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaTransactionStatus from a JSON string
m_pesa_transaction_status_instance = MPesaTransactionStatus.from_json(json)
# print the JSON string representation of the object
print(MPesaTransactionStatus.to_json())

# convert the object into a dict
m_pesa_transaction_status_dict = m_pesa_transaction_status_instance.to_dict()
# create an instance of MPesaTransactionStatus from a dict
m_pesa_transaction_status_from_dict = MPesaTransactionStatus.from_dict(m_pesa_transaction_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


