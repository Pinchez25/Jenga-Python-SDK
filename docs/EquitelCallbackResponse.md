# EquitelCallbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Transaction status | [optional] 
**code** | **int** | Status code | [optional] 
**message** | **str** | Status message | [optional] 
**transaction_reference** | **str** | Transaction reference number | [optional] 
**telco_reference** | **str** | Telco reference number | [optional] 
**mobile_number** | **str** | Payer&#39;s mobile number | [optional] 
**debited_amount** | **float** | Amount debited from payer | [optional] 
**request_amount** | **float** | Original requested amount | [optional] 
**charge** | **float** | Service charge | [optional] 
**currency** | **str** | Transaction currency | [optional] 
**telco** | **str** | Telco provider | [optional] 

## Example

```python
from jenga_client.models.equitel_callback_response import EquitelCallbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EquitelCallbackResponse from a JSON string
equitel_callback_response_instance = EquitelCallbackResponse.from_json(json)
# print the JSON string representation of the object
print(EquitelCallbackResponse.to_json())

# convert the object into a dict
equitel_callback_response_dict = equitel_callback_response_instance.to_dict()
# create an instance of EquitelCallbackResponse from a dict
equitel_callback_response_from_dict = EquitelCallbackResponse.from_dict(equitel_callback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


