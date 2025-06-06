# EquitelPushResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Overall status of the response | [optional] 
**code** | **int** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**reference** | **str** | Payment reference number | [optional] 
**transaction_id** | **str** | Transaction ID | [optional] 

## Example

```python
from jenga_client.models.equitel_push_response import EquitelPushResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EquitelPushResponse from a JSON string
equitel_push_response_instance = EquitelPushResponse.from_json(json)
# print the JSON string representation of the object
print(EquitelPushResponse.to_json())

# convert the object into a dict
equitel_push_response_dict = equitel_push_response_instance.to_dict()
# create an instance of EquitelPushResponse from a dict
equitel_push_response_from_dict = EquitelPushResponse.from_dict(equitel_push_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


