# IMTWithinEquityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**IMTWithinEquityRequestSource**](IMTWithinEquityRequestSource.md) |  | 
**sender** | [**IMTWithinEquityRequestSender**](IMTWithinEquityRequestSender.md) |  | 
**destination** | [**IMTWithinEquityRequestDestination**](IMTWithinEquityRequestDestination.md) |  | 
**transfer** | [**IMTWithinEquityRequestTransfer**](IMTWithinEquityRequestTransfer.md) |  | 

## Example

```python
from jenga_client.models.imt_within_equity_request import IMTWithinEquityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityRequest from a JSON string
imt_within_equity_request_instance = IMTWithinEquityRequest.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityRequest.to_json())

# convert the object into a dict
imt_within_equity_request_dict = imt_within_equity_request_instance.to_dict()
# create an instance of IMTWithinEquityRequest from a dict
imt_within_equity_request_from_dict = IMTWithinEquityRequest.from_dict(imt_within_equity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


