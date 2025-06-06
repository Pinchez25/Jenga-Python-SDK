# EquitelPushRequestPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** | Payment Reference (6-12 alphanumeric characters) | 
**mobile_number** | **str** | Payer&#39;s mobile number with country code prefix | 
**telco** | **str** | Payer&#39;s telco | 
**amount** | **str** | Transaction amount (up to 2 decimal places) | 
**var_date** | **date** | Transaction date in YYYY-MM-DD format | 
**call_back_url** | **str** | Callback URL for transaction status notifications | 
**push_type** | **str** | Type of push notification | 

## Example

```python
from jenga_client.models.equitel_push_request_payment import EquitelPushRequestPayment

# TODO update the JSON string below
json = "{}"
# create an instance of EquitelPushRequestPayment from a JSON string
equitel_push_request_payment_instance = EquitelPushRequestPayment.from_json(json)
# print the JSON string representation of the object
print(EquitelPushRequestPayment.to_json())

# convert the object into a dict
equitel_push_request_payment_dict = equitel_push_request_payment_instance.to_dict()
# create an instance of EquitelPushRequestPayment from a dict
equitel_push_request_payment_from_dict = EquitelPushRequestPayment.from_dict(equitel_push_request_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


