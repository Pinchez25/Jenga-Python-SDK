# EazzyPayMerchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Merchant name | [optional] 
**tillnumber** | **str** | Merchant till number | [optional] 
**outlets** | [**List[EazzyPayMerchantOutletsInner]**](EazzyPayMerchantOutletsInner.md) |  | [optional] 

## Example

```python
from jenga_client.models.eazzy_pay_merchant import EazzyPayMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of EazzyPayMerchant from a JSON string
eazzy_pay_merchant_instance = EazzyPayMerchant.from_json(json)
# print the JSON string representation of the object
print(EazzyPayMerchant.to_json())

# convert the object into a dict
eazzy_pay_merchant_dict = eazzy_pay_merchant_instance.to_dict()
# create an instance of EazzyPayMerchant from a dict
eazzy_pay_merchant_from_dict = EazzyPayMerchant.from_dict(eazzy_pay_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


