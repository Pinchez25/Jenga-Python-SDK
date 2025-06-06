# coding: utf-8

"""
    Jenga API

    API for Jenga payment processing and transaction management

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from jenga_client.models.m_pesa_stk_push_request_payment_details import MPesaStkPushRequestPaymentDetails
from typing import Optional, Set
from typing_extensions import Self

class MPesaStkPushRequestPayment(BaseModel):
    """
    MPesaStkPushRequestPayment
    """ # noqa: E501
    payment_reference: StrictStr = Field(description="Payment reference, should be unique per request", alias="paymentReference")
    payment_currency: StrictStr = Field(description="Currency of the payment", alias="paymentCurrency")
    channel: StrictStr = Field(description="Channel of the payment")
    service: StrictStr = Field(description="Payment service")
    provider: StrictStr = Field(description="Payment provider")
    callback_url: StrictStr = Field(description="Callback URL for transaction status", alias="callbackUrl")
    details: MPesaStkPushRequestPaymentDetails
    __properties: ClassVar[List[str]] = ["paymentReference", "paymentCurrency", "channel", "service", "provider", "callbackUrl", "details"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MPesaStkPushRequestPayment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MPesaStkPushRequestPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentReference": obj.get("paymentReference"),
            "paymentCurrency": obj.get("paymentCurrency"),
            "channel": obj.get("channel"),
            "service": obj.get("service"),
            "provider": obj.get("provider"),
            "callbackUrl": obj.get("callbackUrl"),
            "details": MPesaStkPushRequestPaymentDetails.from_dict(obj["details"]) if obj.get("details") is not None else None
        })
        return _obj


