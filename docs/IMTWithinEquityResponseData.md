# IMTWithinEquityResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Unique transaction ID | [optional] 
**status** | **str** | Transaction status | [optional] 

## Example

```python
from jenga_client.models.imt_within_equity_response_data import IMTWithinEquityResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityResponseData from a JSON string
imt_within_equity_response_data_instance = IMTWithinEquityResponseData.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityResponseData.to_json())

# convert the object into a dict
imt_within_equity_response_data_dict = imt_within_equity_response_data_instance.to_dict()
# create an instance of IMTWithinEquityResponseData from a dict
imt_within_equity_response_data_from_dict = IMTWithinEquityResponseData.from_dict(imt_within_equity_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


