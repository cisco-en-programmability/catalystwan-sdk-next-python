# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface
import logging


class TemplateBuilder:
    """
    Builds and executes requests for operations under /networkdesign/profile/template
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_profile_template_list(self, **kw) -> List[Any]:
        """
        Generate profile template list

        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "generateProfileTemplateList")
        return self._request_adapter.request(
            "GET",
            "/dataservice/networkdesign/profile/template",
            return_type=List[Any],
            **kw,
        )

    def get_device_profile_template(self, template_id: str, **kw) -> Any:
        """
        Get device profile template

        :param template_id: Template Id
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getDeviceProfileTemplate")
        params = {
            "templateId": template_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/networkdesign/profile/template/{templateId}",
            params=params,
            **kw,
        )

    @property
    def edit_device_profile_template(self):
        class edit_device_profile_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, template_id: str, payload: Optional[Any] = None, **kw):
                """
                Edit device profile template

                :param template_id: Template Id
                :param payload: Global template
                :returns: None
                """
                logging.warning(
                    "Operation: %s is deprecated", "editDeviceProfileTemplate"
                )
                params = {
                    "templateId": template_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/networkdesign/profile/template/{templateId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_device_profile_template_(self._request_adapter)
