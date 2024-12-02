# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ValidateTemplatePostRequest


class VerifyBuilder:
    """
    Builds and executes requests for operations under /template/device/config/verify
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def validate_template(self):
        class validate_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[ValidateTemplatePostRequest] = None, **kw
            ):
                """
                Validate full template"



                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Payload
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "validateTemplate")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/device/config/verify",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> ValidateTemplatePostRequest:
                return ValidateTemplatePostRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[ValidateTemplatePostRequest]:
                return ValidateTemplatePostRequest

        return validate_template_(self._request_adapter)
