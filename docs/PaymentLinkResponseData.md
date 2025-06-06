# PaymentLinkResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **int** | Timestamp of creation | [optional] 
**payment_link_ref** | **str** | Payment link reference | [optional] 
**external_ref** | **str** | External reference | [optional] 
**status** | [**PaymentLinkResponseDataStatus**](PaymentLinkResponseDataStatus.md) |  | [optional] 

## Example

```python
from jenga_client.models.payment_link_response_data import PaymentLinkResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLinkResponseData from a JSON string
payment_link_response_data_instance = PaymentLinkResponseData.from_json(json)
# print the JSON string representation of the object
print(PaymentLinkResponseData.to_json())

# convert the object into a dict
payment_link_response_data_dict = payment_link_response_data_instance.to_dict()
# create an instance of PaymentLinkResponseData from a dict
payment_link_response_data_from_dict = PaymentLinkResponseData.from_dict(payment_link_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


