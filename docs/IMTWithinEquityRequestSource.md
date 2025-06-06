# IMTWithinEquityRequestSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country code of the source account | 
**name** | **str** | The name of the source account holder | 
**account_number** | **str** | The account number of the source account | 

## Example

```python
from jenga_client.models.imt_within_equity_request_source import IMTWithinEquityRequestSource

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityRequestSource from a JSON string
imt_within_equity_request_source_instance = IMTWithinEquityRequestSource.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityRequestSource.to_json())

# convert the object into a dict
imt_within_equity_request_source_dict = imt_within_equity_request_source_instance.to_dict()
# create an instance of IMTWithinEquityRequestSource from a dict
imt_within_equity_request_source_from_dict = IMTWithinEquityRequestSource.from_dict(imt_within_equity_request_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


