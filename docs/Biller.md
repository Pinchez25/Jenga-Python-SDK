# Biller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller_code** | **str** | Biller code | [optional] 
**biller_name** | **str** | Biller name | [optional] 
**country_code** | **str** | Country code | [optional] 
**category** | **str** | Biller category | [optional] 

## Example

```python
from jenga_client.models.biller import Biller

# TODO update the JSON string below
json = "{}"
# create an instance of Biller from a JSON string
biller_instance = Biller.from_json(json)
# print the JSON string representation of the object
print(Biller.to_json())

# convert the object into a dict
biller_dict = biller_instance.to_dict()
# create an instance of Biller from a dict
biller_from_dict = Biller.from_dict(biller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


