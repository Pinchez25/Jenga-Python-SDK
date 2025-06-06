# MPesaTransactionStatusDataOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_amount** | **float** | Request amount | [optional] 
**amount_paid** | **float** | Amount paid by customer including service charge | [optional] 
**order_reference** | **str** | Order Reference | [optional] 
**order_status** | **str** | Status of an order (Paid, Pending) | [optional] 
**created_on** | **float** | Creation date of the order in EPOC time | [optional] 

## Example

```python
from jenga_client.models.m_pesa_transaction_status_data_order import MPesaTransactionStatusDataOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaTransactionStatusDataOrder from a JSON string
m_pesa_transaction_status_data_order_instance = MPesaTransactionStatusDataOrder.from_json(json)
# print the JSON string representation of the object
print(MPesaTransactionStatusDataOrder.to_json())

# convert the object into a dict
m_pesa_transaction_status_data_order_dict = m_pesa_transaction_status_data_order_instance.to_dict()
# create an instance of MPesaTransactionStatusDataOrder from a dict
m_pesa_transaction_status_data_order_from_dict = MPesaTransactionStatusDataOrder.from_dict(m_pesa_transaction_status_data_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


