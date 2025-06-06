# EquitelPushRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant** | [**EquitelPushRequestMerchant**](EquitelPushRequestMerchant.md) |  | 
**payment** | [**EquitelPushRequestPayment**](EquitelPushRequestPayment.md) |  | 

## Example

```python
from jenga_client.models.equitel_push_request import EquitelPushRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EquitelPushRequest from a JSON string
equitel_push_request_instance = EquitelPushRequest.from_json(json)
# print the JSON string representation of the object
print(EquitelPushRequest.to_json())

# convert the object into a dict
equitel_push_request_dict = equitel_push_request_instance.to_dict()
# create an instance of EquitelPushRequest from a dict
equitel_push_request_from_dict = EquitelPushRequest.from_dict(equitel_push_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


