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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MPesaTransactionStatusDataInvoicesInner(BaseModel):
    """
    MPesaTransactionStatusDataInvoicesInner
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Invoice Amount")
    amount_debited: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount paid by the customer", alias="amountDebited")
    charge: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Service charge")
    invoice_status: Optional[StrictStr] = Field(default=None, description="Status of invoice (Pending, Paid, Cancelled, Expired)", alias="invoiceStatus")
    order_reference: Optional[StrictStr] = Field(default=None, description="Order Reference", alias="orderReference")
    external_reference: Optional[StrictStr] = Field(default=None, description="Mpesa Reference", alias="externalReference")
    created_on: Optional[StrictStr] = Field(default=None, description="Date invoice was generated", alias="createdOn")
    completed_on: Optional[StrictStr] = Field(default=None, description="Date Payment was completed", alias="completedOn")
    __properties: ClassVar[List[str]] = ["amount", "amountDebited", "charge", "invoiceStatus", "orderReference", "externalReference", "createdOn", "completedOn"]

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
        """Create an instance of MPesaTransactionStatusDataInvoicesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MPesaTransactionStatusDataInvoicesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "amountDebited": obj.get("amountDebited"),
            "charge": obj.get("charge"),
            "invoiceStatus": obj.get("invoiceStatus"),
            "orderReference": obj.get("orderReference"),
            "externalReference": obj.get("externalReference"),
            "createdOn": obj.get("createdOn"),
            "completedOn": obj.get("completedOn")
        })
        return _obj


