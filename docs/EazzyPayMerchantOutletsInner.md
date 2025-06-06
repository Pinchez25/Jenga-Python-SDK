# EazzyPayMerchantOutletsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Merchant outlet name | [optional] 
**tillnumber** | **str** | Merchant outlet till number | [optional] 

## Example

```python
from jenga_client.models.eazzy_pay_merchant_outlets_inner import EazzyPayMerchantOutletsInner

# TODO update the JSON string below
json = "{}"
# create an instance of EazzyPayMerchantOutletsInner from a JSON string
eazzy_pay_merchant_outlets_inner_instance = EazzyPayMerchantOutletsInner.from_json(json)
# print the JSON string representation of the object
print(EazzyPayMerchantOutletsInner.to_json())

# convert the object into a dict
eazzy_pay_merchant_outlets_inner_dict = eazzy_pay_merchant_outlets_inner_instance.to_dict()
# create an instance of EazzyPayMerchantOutletsInner from a dict
eazzy_pay_merchant_outlets_inner_from_dict = EazzyPayMerchantOutletsInner.from_dict(eazzy_pay_merchant_outlets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


