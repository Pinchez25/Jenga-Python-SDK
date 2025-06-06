# PaymentLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**List[PaymentLinkRequestCustomersInner]**](PaymentLinkRequestCustomersInner.md) |  | 
**payment_link** | [**PaymentLinkRequestPaymentLink**](PaymentLinkRequestPaymentLink.md) |  | 
**notifications** | **List[str]** | Modes for customer to receive payment link | [optional] 

## Example

```python
from jenga_client.models.payment_link_request import PaymentLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkRequest from a JSON string
payment_link_request_instance = PaymentLinkRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkRequest.to_json())

# convert the object into a dict
payment_link_request_dict = payment_link_request_instance.to_dict()
# create an instance of PaymentLinkRequest from a dict
payment_link_request_from_dict = PaymentLinkRequest.from_dict(payment_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


