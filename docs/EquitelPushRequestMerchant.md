# EquitelPushRequestMerchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Merchant country code | 
**account_number** | **str** | Account number to be credited on payment completion | 
**name** | **str** | Merchant name | 

## Example

```python
from jenga_client.models.equitel_push_request_merchant import EquitelPushRequestMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of EquitelPushRequestMerchant from a JSON string
equitel_push_request_merchant_instance = EquitelPushRequestMerchant.from_json(json)
# print the JSON string representation of the object
print(EquitelPushRequestMerchant.to_json())

# convert the object into a dict
equitel_push_request_merchant_dict = equitel_push_request_merchant_instance.to_dict()
# create an instance of EquitelPushRequestMerchant from a dict
equitel_push_request_merchant_from_dict = EquitelPushRequestMerchant.from_dict(equitel_push_request_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


