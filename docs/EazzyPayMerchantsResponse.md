# EazzyPayMerchantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchants** | [**List[EazzyPayMerchant]**](EazzyPayMerchant.md) |  | [optional] 

## Example

```python
from jenga_client.models.eazzy_pay_merchants_response import EazzyPayMerchantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EazzyPayMerchantsResponse from a JSON string
eazzy_pay_merchants_response_instance = EazzyPayMerchantsResponse.from_json(json)
# print the JSON string representation of the object
print(EazzyPayMerchantsResponse.to_json())

# convert the object into a dict
eazzy_pay_merchants_response_dict = eazzy_pay_merchants_response_instance.to_dict()
# create an instance of EazzyPayMerchantsResponse from a dict
eazzy_pay_merchants_response_from_dict = EazzyPayMerchantsResponse.from_dict(eazzy_pay_merchants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


