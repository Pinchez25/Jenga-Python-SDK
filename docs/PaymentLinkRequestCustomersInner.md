# PaymentLinkRequestCustomersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First Name of the customer | 
**last_name** | **str** | Last Name of the customer | 
**email** | **str** | Customer Email | 
**phone_number** | **str** | Customer phone number | [optional] 
**first_address** | **str** | Physical Address | [optional] 
**country_code** | **str** | Alpha-2 country code | 
**postal_or_zip_code** | **str** | Postal or Zip Code | [optional] 
**customer_external_ref** | **str** | Unique identifier for customer | [optional] 

## Example

```python
from jenga_client.models.payment_link_request_customers_inner import PaymentLinkRequestCustomersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkRequestCustomersInner from a JSON string
payment_link_request_customers_inner_instance = PaymentLinkRequestCustomersInner.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkRequestCustomersInner.to_json())

# convert the object into a dict
payment_link_request_customers_inner_dict = payment_link_request_customers_inner_instance.to_dict()
# create an instance of PaymentLinkRequestCustomersInner from a dict
payment_link_request_customers_inner_from_dict = PaymentLinkRequestCustomersInner.from_dict(payment_link_request_customers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


