# IMTWithinEquityRequestDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of destination | 
**country_code** | **str** | The country code of the destination account | 
**name** | **str** | The name of the destination account holder | 
**bank_code** | **str** | The bank code of the recipient&#39;s bank | 
**account_number** | **str** | The account number of the recipient | 
**mobile_number** | **str** | The mobile number of the recipient | 
**document_type** | **str** | The document type of the recipient | 
**document_number** | **str** | The document number of the recipient | 
**email** | **str** | The email address of the recipient | [optional] 
**address** | **str** | The address of the recipient | [optional] 

## Example

```python
from jenga_client.models.imt_within_equity_request_destination import IMTWithinEquityRequestDestination

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityRequestDestination from a JSON string
imt_within_equity_request_destination_instance = IMTWithinEquityRequestDestination.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityRequestDestination.to_json())

# convert the object into a dict
imt_within_equity_request_destination_dict = imt_within_equity_request_destination_instance.to_dict()
# create an instance of IMTWithinEquityRequestDestination from a dict
imt_within_equity_request_destination_from_dict = IMTWithinEquityRequestDestination.from_dict(imt_within_equity_request_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


