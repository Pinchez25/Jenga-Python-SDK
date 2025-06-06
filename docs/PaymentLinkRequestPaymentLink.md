# PaymentLinkRequestPaymentLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **date** | Link Expiry date (yyyy-MM-dd) | 
**sale_date** | **date** | Date service or product offered (yyyy-MM-dd) | 
**sale_type** | **str** | Type of sale | 
**payment_link_type** | **str** | Type of payment link | 
**name** | **str** | Name of product or Service | 
**description** | **str** | Description of service or product | 
**external_ref** | **str** | Third Party reference | 
**payment_link_ref** | **str** | Link reference for updating link details | [optional] 
**redirect_url** | **str** | Website URL to redirect to on successful payment | [optional] 
**amount_option** | **str** | Allow change amount or not | 
**amount** | **float** | Payment Link amount | 
**currency** | **str** | Payment currency | 

## Example

```python
from jenga_client.models.payment_link_request_payment_link import PaymentLinkRequestPaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkRequestPaymentLink from a JSON string
payment_link_request_payment_link_instance = PaymentLinkRequestPaymentLink.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkRequestPaymentLink.to_json())

# convert the object into a dict
payment_link_request_payment_link_dict = payment_link_request_payment_link_instance.to_dict()
# create an instance of PaymentLinkRequestPaymentLink from a dict
payment_link_request_payment_link_from_dict = PaymentLinkRequestPaymentLink.from_dict(payment_link_request_payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


