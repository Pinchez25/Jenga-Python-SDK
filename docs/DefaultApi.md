# jenga_client.DefaultApi

All URIs are relative to *https://api.finserve.africa*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_checkout_api_v1_create_payment_link_post**](DefaultApi.md#api_checkout_api_v1_create_payment_link_post) | **POST** /api-checkout/api/v1/create/payment-link | Create Payment Link
[**api_checkout_mpesa_stk_push_v30_init_post**](DefaultApi.md#api_checkout_mpesa_stk_push_v30_init_post) | **POST** /api-checkout/mpesa-stk-push/v3.0/init | Initiate M-Pesa STK Push
[**api_checkout_mpesa_stk_push_v30_status_order_reference_get**](DefaultApi.md#api_checkout_mpesa_stk_push_v30_status_order_reference_get) | **GET** /api-checkout/mpesa-stk-push/v3.0/status/order/{reference} | Query M-Pesa STK Push Order Status
[**authentication_api_v3_authenticate_merchant_post**](DefaultApi.md#authentication_api_v3_authenticate_merchant_post) | **POST** /authentication/api/v3/authenticate/merchant | Authenticate merchant
[**v3_apis_payment_api_v30_stkussdpush_initiate_post**](DefaultApi.md#v3_apis_payment_api_v30_stkussdpush_initiate_post) | **POST** /v3-apis/payment-api/v3.0/stkussdpush/initiate | Initiate Equitel STK/USSD Push
[**v3_apis_transaction_api_v30_billers_get**](DefaultApi.md#v3_apis_transaction_api_v30_billers_get) | **GET** /v3-apis/transaction-api/v3.0/billers | Get All Billers
[**v3_apis_transaction_api_v30_bills_pay_post**](DefaultApi.md#v3_apis_transaction_api_v30_bills_pay_post) | **POST** /v3-apis/transaction-api/v3.0/bills/pay | Initiate bill payment
[**v3_apis_transaction_api_v30_bills_validation_post**](DefaultApi.md#v3_apis_transaction_api_v30_bills_validation_post) | **POST** /v3-apis/transaction-api/v3.0/bills/validation | Validate bill
[**v3_apis_transaction_api_v30_merchants_get**](DefaultApi.md#v3_apis_transaction_api_v30_merchants_get) | **GET** /v3-apis/transaction-api/v3.0/merchants | Get All EazzyPay Merchants
[**v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post**](DefaultApi.md#v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post) | **POST** /v3-apis/transaction-api/v3.0/remittance/internalBankTransfer/imt | IMT Within Equity Bank
[**v3_apis_transaction_api_v30_transaction_transaction_id_get**](DefaultApi.md#v3_apis_transaction_api_v30_transaction_transaction_id_get) | **GET** /v3-apis/transaction-api/v3.0/transaction/{transactionId} | Get Transaction Details


# **api_checkout_api_v1_create_payment_link_post**
> PaymentLinkResponse api_checkout_api_v1_create_payment_link_post(payment_link_request)

Create Payment Link

Creates a payment link that can be sent to customers via SMS or email.
Supports both single and bulk payment links.


### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.payment_link_request import PaymentLinkRequest
from jenga_client.models.payment_link_response import PaymentLinkResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    payment_link_request = jenga_client.PaymentLinkRequest() # PaymentLinkRequest | 

    try:
        # Create Payment Link
        api_response = api_instance.api_checkout_api_v1_create_payment_link_post(payment_link_request)
        print("The response of DefaultApi->api_checkout_api_v1_create_payment_link_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_checkout_api_v1_create_payment_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_link_request** | [**PaymentLinkRequest**](PaymentLinkRequest.md)|  | 

### Return type

[**PaymentLinkResponse**](PaymentLinkResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment link created successfully |  -  |
**400** | Invalid request or payment already completed |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_checkout_mpesa_stk_push_v30_init_post**
> MPesaStkPushResponse api_checkout_mpesa_stk_push_v30_init_post(m_pesa_stk_push_request)

Initiate M-Pesa STK Push

Initiates M-Pesa STK push for payment transactions.
Supports both wallet-based and account-based settlement.


### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.m_pesa_stk_push_request import MPesaStkPushRequest
from jenga_client.models.m_pesa_stk_push_response import MPesaStkPushResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    m_pesa_stk_push_request = jenga_client.MPesaStkPushRequest() # MPesaStkPushRequest | 

    try:
        # Initiate M-Pesa STK Push
        api_response = api_instance.api_checkout_mpesa_stk_push_v30_init_post(m_pesa_stk_push_request)
        print("The response of DefaultApi->api_checkout_mpesa_stk_push_v30_init_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_checkout_mpesa_stk_push_v30_init_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **m_pesa_stk_push_request** | [**MPesaStkPushRequest**](MPesaStkPushRequest.md)|  | 

### Return type

[**MPesaStkPushResponse**](MPesaStkPushResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction initiated successfully |  -  |
**401** | Not authorized to access this Telco |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_checkout_mpesa_stk_push_v30_status_order_reference_get**
> MPesaStkPushResponse api_checkout_mpesa_stk_push_v30_status_order_reference_get(reference)

Query M-Pesa STK Push Order Status

Check the status of an M-Pesa STK push transaction

### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.m_pesa_stk_push_response import MPesaStkPushResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    reference = 'reference_example' # str | Order reference number

    try:
        # Query M-Pesa STK Push Order Status
        api_response = api_instance.api_checkout_mpesa_stk_push_v30_status_order_reference_get(reference)
        print("The response of DefaultApi->api_checkout_mpesa_stk_push_v30_status_order_reference_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_checkout_mpesa_stk_push_v30_status_order_reference_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| Order reference number | 

### Return type

[**MPesaStkPushResponse**](MPesaStkPushResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order status retrieved successfully |  -  |
**401** | Authentication failed |  -  |
**404** | Order not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_api_v3_authenticate_merchant_post**
> AuthenticationResponse authentication_api_v3_authenticate_merchant_post(authentication_request)

Authenticate merchant

Authenticate a merchant and get an access token

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import jenga_client
from jenga_client.models.authentication_request import AuthenticationRequest
from jenga_client.models.authentication_response import AuthenticationResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    authentication_request = jenga_client.AuthenticationRequest() # AuthenticationRequest | 

    try:
        # Authenticate merchant
        api_response = api_instance.authentication_api_v3_authenticate_merchant_post(authentication_request)
        print("The response of DefaultApi->authentication_api_v3_authenticate_merchant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->authentication_api_v3_authenticate_merchant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_request** | [**AuthenticationRequest**](AuthenticationRequest.md)|  | 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful authentication |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_payment_api_v30_stkussdpush_initiate_post**
> EquitelPushResponse v3_apis_payment_api_v30_stkussdpush_initiate_post(equitel_push_request)

Initiate Equitel STK/USSD Push

Initiates STK or USSD pushes to Telco MNOs for payment transactions via Equitel.
STK Push allows a customer to select an account to debit from whereas for USSD Push it debits the primary account of the customer.


### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.equitel_push_request import EquitelPushRequest
from jenga_client.models.equitel_push_response import EquitelPushResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    equitel_push_request = jenga_client.EquitelPushRequest() # EquitelPushRequest | 

    try:
        # Initiate Equitel STK/USSD Push
        api_response = api_instance.v3_apis_payment_api_v30_stkussdpush_initiate_post(equitel_push_request)
        print("The response of DefaultApi->v3_apis_payment_api_v30_stkussdpush_initiate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_payment_api_v30_stkussdpush_initiate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equitel_push_request** | [**EquitelPushRequest**](EquitelPushRequest.md)|  | 

### Return type

[**EquitelPushResponse**](EquitelPushResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction initiated successfully |  -  |
**400** | Invalid request or duplicate transaction |  -  |
**401** | Not authorized to access this Telco |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_billers_get**
> BillersResponse v3_apis_transaction_api_v30_billers_get()

Get All Billers

Returns a list of all available billers

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.billers_response import BillersResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)

    try:
        # Get All Billers
        api_response = api_instance.v3_apis_transaction_api_v30_billers_get()
        print("The response of DefaultApi->v3_apis_transaction_api_v30_billers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_billers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BillersResponse**](BillersResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billers retrieved successfully |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_bills_pay_post**
> BillPaymentResponse v3_apis_transaction_api_v30_bills_pay_post(bill_payment_request)

Initiate bill payment

Provides partners the capability to initiate utility bill payments for goods and services

### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.bill_payment_request import BillPaymentRequest
from jenga_client.models.bill_payment_response import BillPaymentResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    bill_payment_request = jenga_client.BillPaymentRequest() # BillPaymentRequest | 

    try:
        # Initiate bill payment
        api_response = api_instance.v3_apis_transaction_api_v30_bills_pay_post(bill_payment_request)
        print("The response of DefaultApi->v3_apis_transaction_api_v30_bills_pay_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_bills_pay_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_payment_request** | [**BillPaymentRequest**](BillPaymentRequest.md)|  | 

### Return type

[**BillPaymentResponse**](BillPaymentResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bill payment processed successfully |  -  |
**401** | Authentication failed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_bills_validation_post**
> BillValidationResponse v3_apis_transaction_api_v30_bills_validation_post(bill_validation_request)

Validate bill

Enables your application to perform a bill validation before making a payment

### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.bill_validation_request import BillValidationRequest
from jenga_client.models.bill_validation_response import BillValidationResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    bill_validation_request = jenga_client.BillValidationRequest() # BillValidationRequest | 

    try:
        # Validate bill
        api_response = api_instance.v3_apis_transaction_api_v30_bills_validation_post(bill_validation_request)
        print("The response of DefaultApi->v3_apis_transaction_api_v30_bills_validation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_bills_validation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_validation_request** | [**BillValidationRequest**](BillValidationRequest.md)|  | 

### Return type

[**BillValidationResponse**](BillValidationResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Bill validation successful |  -  |
**401** | Authentication failed |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_merchants_get**
> EazzyPayMerchantsResponse v3_apis_transaction_api_v30_merchants_get(per_page=per_page, page=page)

Get All EazzyPay Merchants

Returns a list of all EazzyPay merchants and their outlets

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.eazzy_pay_merchants_response import EazzyPayMerchantsResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    per_page = 56 # int | Number of results per page (optional)
    page = 56 # int | Page number (optional)

    try:
        # Get All EazzyPay Merchants
        api_response = api_instance.v3_apis_transaction_api_v30_merchants_get(per_page=per_page, page=page)
        print("The response of DefaultApi->v3_apis_transaction_api_v30_merchants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_merchants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of results per page | [optional] 
 **page** | **int**| Page number | [optional] 

### Return type

[**EazzyPayMerchantsResponse**](EazzyPayMerchantsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Merchants retrieved successfully |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post**
> IMTWithinEquityResponse v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post(imt_within_equity_request)

IMT Within Equity Bank

Move funds within Equity Bank across Kenya, Uganda, Tanzania, Rwanda & South Sudan.
Supports internal money transfers between Equity Bank accounts.


### Example

* Api Key Authentication (SignatureAuth):
* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.imt_within_equity_request import IMTWithinEquityRequest
from jenga_client.models.imt_within_equity_response import IMTWithinEquityResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: SignatureAuth
configuration.api_key['SignatureAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SignatureAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    imt_within_equity_request = jenga_client.IMTWithinEquityRequest() # IMTWithinEquityRequest | 

    try:
        # IMT Within Equity Bank
        api_response = api_instance.v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post(imt_within_equity_request)
        print("The response of DefaultApi->v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_remittance_internal_bank_transfer_imt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imt_within_equity_request** | [**IMTWithinEquityRequest**](IMTWithinEquityRequest.md)|  | 

### Return type

[**IMTWithinEquityResponse**](IMTWithinEquityResponse.md)

### Authorization

[SignatureAuth](../README.md#SignatureAuth), [ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer initiated successfully |  -  |
**400** | Invalid request |  -  |
**401** | Authentication failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_apis_transaction_api_v30_transaction_transaction_id_get**
> TransactionDetailsResponse v3_apis_transaction_api_v30_transaction_transaction_id_get(transaction_id)

Get Transaction Details

Retrieves details of a specific transaction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer Authentication (BearerAuth):

```python
import jenga_client
from jenga_client.models.transaction_details_response import TransactionDetailsResponse
from jenga_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.finserve.africa
# See configuration.py for a list of all supported configuration parameters.
configuration = jenga_client.Configuration(
    host = "https://api.finserve.africa"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization: BearerAuth
configuration = jenga_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with jenga_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jenga_client.DefaultApi(api_client)
    transaction_id = 'transaction_id_example' # str | Transaction ID

    try:
        # Get Transaction Details
        api_response = api_instance.v3_apis_transaction_api_v30_transaction_transaction_id_get(transaction_id)
        print("The response of DefaultApi->v3_apis_transaction_api_v30_transaction_transaction_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->v3_apis_transaction_api_v30_transaction_transaction_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| Transaction ID | 

### Return type

[**TransactionDetailsResponse**](TransactionDetailsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction details retrieved successfully |  -  |
**401** | Authentication failed |  -  |
**404** | Transaction not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

