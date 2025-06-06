# IMTWithinEquityRequestSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the sender | 
**document_type** | **str** | The type of document | 
**document_number** | **str** | The document number of the sender | 
**country_code** | **str** | The country code of the sender | 
**mobile_number** | **str** | The mobile number of the sender | 
**email** | **str** | The email address of the sender | 
**address** | **str** | The address of the sender | [optional] 

## Example

```python
from jenga_client.models.imt_within_equity_request_sender import IMTWithinEquityRequestSender

# TODO update the JSON string below
json = "{}"
# create an instance of IMTWithinEquityRequestSender from a JSON string
imt_within_equity_request_sender_instance = IMTWithinEquityRequestSender.from_json(json)
# print the JSON string representation of the object
print(IMTWithinEquityRequestSender.to_json())

# convert the object into a dict
imt_within_equity_request_sender_dict = imt_within_equity_request_sender_instance.to_dict()
# create an instance of IMTWithinEquityRequestSender from a dict
imt_within_equity_request_sender_from_dict = IMTWithinEquityRequestSender.from_dict(imt_within_equity_request_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


