# AuthenticationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_code** | **str** | Merchant code for authentication | 
**consumer_secret** | **str** | Consumer secret for authentication | 

## Example

```python
from jenga_client.models.authentication_request import AuthenticationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationRequest from a JSON string
authentication_request_instance = AuthenticationRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticationRequest.to_json())

# convert the object into a dict
authentication_request_dict = authentication_request_instance.to_dict()
# create an instance of AuthenticationRequest from a dict
authentication_request_from_dict = AuthenticationRequest.from_dict(authentication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


