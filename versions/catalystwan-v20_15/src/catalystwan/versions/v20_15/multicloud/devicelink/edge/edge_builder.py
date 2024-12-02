# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
import logging
from .models import EdgeTypeParam

if TYPE_CHECKING:
    from .portspeed.portspeed_builder import PortspeedBuilder


class EdgeBuilder:
    """
    Builds and executes requests for operations under /multicloud/devicelink/edge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_device_links(
        self,
        edge_type: Optional[EdgeTypeParam] = None,
        device_link_name: Optional[str] = None,
        **kw,
    ) -> Any:
        """
        Get Device Links

        :param edge_type: Edge type
        :param device_link_name: Device Link Name
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getDeviceLinks")
        params = {
            "edgeType": edge_type,
            "deviceLinkName": device_link_name,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/multicloud/devicelink/edge", params=params, **kw
        )

    @property
    def update_device_link(self):
        class update_device_link_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Update Device Link

                :param payload: Device Link
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "updateDeviceLink")
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/devicelink/edge",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_device_link_(self._request_adapter)

    @property
    def create_device_link(self):
        class create_device_link_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create Device Link

                :param payload: Device Link
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "createDeviceLink")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/devicelink/edge",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_device_link_(self._request_adapter)

    def delete_device_link(self, device_link_name: str, **kw) -> Any:
        """
        Delete Device Link

        :param device_link_name: Device Link Name
        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "deleteDeviceLink")
        params = {
            "deviceLinkName": device_link_name,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/devicelink/edge/{deviceLinkName}",
            params=params,
            **kw,
        )

    @property
    def portspeed(self) -> PortspeedBuilder:
        """
        The portspeed property
        """
        from .portspeed.portspeed_builder import PortspeedBuilder

        return PortspeedBuilder(self._request_adapter)
