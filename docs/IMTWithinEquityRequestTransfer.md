# IMTWithinEquityRequestTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of transfer | 
**amount** | **str** | The amount to be transferred | 
**currency_code** | **str** | The currency code | 
**reference** | **str** | The reference number for the transfer | 
**var_date** | **date** | The date of the transfer | 
**description** | **str** | A description of the transfer | [optional] 

## Example

```python
from jenga_client.models.imt_within_equity_request_transfer import IMTWithinEquityRequestTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityRequestTransfer from a JSON string
imt_within_equity_request_transfer_instance = IMTWithinEquityRequestTransfer.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityRequestTransfer.to_json())

# convert the object into a dict
imt_within_equity_request_transfer_dict = imt_within_equity_request_transfer_instance.to_dict()
# create an instance of IMTWithinEquityRequestTransfer from a dict
imt_within_equity_request_transfer_from_dict = IMTWithinEquityRequestTransfer.from_dict(imt_within_equity_request_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


