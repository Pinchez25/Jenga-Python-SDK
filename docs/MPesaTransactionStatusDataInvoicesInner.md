# MPesaTransactionStatusDataInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Invoice Amount | [optional] 
**amount_debited** | **float** | Amount paid by the customer | [optional] 
**charge** | **float** | Service charge | [optional] 
**invoice_status** | **str** | Status of invoice (Pending, Paid, Cancelled, Expired) | [optional] 
**order_reference** | **str** | Order Reference | [optional] 
**external_reference** | **str** | Mpesa Reference | [optional] 
**created_on** | **str** | Date invoice was generated | [optional] 
**completed_on** | **str** | Date Payment was completed | [optional] 

## Example

```python
from jenga_client.models.m_pesa_transaction_status_data_invoices_inner import MPesaTransactionStatusDataInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MPesaTransactionStatusDataInvoicesInner from a JSON string
m_pesa_transaction_status_data_invoices_inner_instance = MPesaTransactionStatusDataInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(MPesaTransactionStatusDataInvoicesInner.to_json())

# convert the object into a dict
m_pesa_transaction_status_data_invoices_inner_dict = m_pesa_transaction_status_data_invoices_inner_instance.to_dict()
# create an instance of MPesaTransactionStatusDataInvoicesInner from a dict
m_pesa_transaction_status_data_invoices_inner_from_dict = MPesaTransactionStatusDataInvoicesInner.from_dict(m_pesa_transaction_status_data_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


