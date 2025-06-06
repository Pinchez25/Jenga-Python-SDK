# PaymentLinkResponseDataStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Status code | [optional] 
**name** | **str** | Status name | [optional] 

## Example

```python
from jenga_client.models.payment_link_response_data_status import PaymentLinkResponseDataStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponseDataStatus from a JSON string
payment_link_response_data_status_instance = PaymentLinkResponseDataStatus.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponseDataStatus.to_json())

# convert the object into a dict
payment_link_response_data_status_dict = payment_link_response_data_status_instance.to_dict()
# create an instance of PaymentLinkResponseDataStatus from a dict
payment_link_response_data_status_from_dict = PaymentLinkResponseDataStatus.from_dict(payment_link_response_data_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


