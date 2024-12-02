# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type
from catalystwan.abc import RequestAdapterInterface


class LiBuilder:
    """
    Builds and executes requests for operations under /template/feature/li
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_li_template(self, **kw) -> List[Any]:
        """
        Get LI feature template

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/feature/li", return_type=List[Any], **kw
        )

    @property
    def create_li_template(self):
        class create_li_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create LI feature template


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: LI template
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/template/feature/li", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_li_template_(self._request_adapter)

    @property
    def edit_li_template(self):
        class edit_li_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, template_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Update LI feature template


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param template_id: Template Id
                :param payload: LI template
                :returns: Any
                """
                params = {
                    "templateId": template_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/feature/li/{templateId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_li_template_(self._request_adapter)
