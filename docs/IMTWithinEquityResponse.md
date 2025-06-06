# IMTWithinEquityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status | [optional] 
**code** | **int** | Response code | [optional] 
**message** | **str** | Response message | [optional] 
**data** | [**IMTWithinEquityResponseData**](IMTWithinEquityResponseData.md) |  | [optional] 

## Example

```python
from jenga_client.models.imt_within_equity_response import IMTWithinEquityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityResponse from a JSON string
imt_within_equity_response_instance = IMTWithinEquityResponse.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityResponse.to_json())

# convert the object into a dict
imt_within_equity_response_dict = imt_within_equity_response_instance.to_dict()
# create an instance of IMTWithinEquityResponse from a dict
imt_within_equity_response_from_dict = IMTWithinEquityResponse.from_dict(imt_within_equity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


