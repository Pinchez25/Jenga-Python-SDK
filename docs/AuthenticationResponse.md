# AuthenticationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | JWT access token | [optional] 
**expires_in** | **datetime** | Token expiration timestamp | [optional] 
**issued_at** | **datetime** | When the token was issued | [optional] 
**token_type** | **str** | Type of token | [optional] 
**refresh_token** | **str** | Token used to refresh the access token | [optional] 

## Example

```python
from jenga_client.models.authentication_response import AuthenticationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationResponse from a JSON string
authentication_response_instance = AuthenticationResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationResponse.to_json())

# convert the object into a dict
authentication_response_dict = authentication_response_instance.to_dict()
# create an instance of AuthenticationResponse from a dict
authentication_response_from_dict = AuthenticationResponse.from_dict(authentication_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


