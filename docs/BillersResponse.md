# BillersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **str** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**data** | [**List[Biller]**](Biller.md) |  | [optional] 

## Example

```python
from jenga_client.models.billers_response import BillersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillersResponse from a JSON string
billers_response_instance = BillersResponse.from_json(json)
# print the JSON string representation of the object
print(BillersResponse.to_json())

# convert the object into a dict
billers_response_dict = billers_response_instance.to_dict()
# create an instance of BillersResponse from a dict
billers_response_from_dict = BillersResponse.from_dict(billers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


