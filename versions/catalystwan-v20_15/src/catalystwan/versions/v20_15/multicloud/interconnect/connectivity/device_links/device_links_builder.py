# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import InterconnectDeviceLink, InterconnectTypeParam, ProcessResponse

if TYPE_CHECKING:
    from .metro_speed.metro_speed_builder import MetroSpeedBuilder
    from .port_speeds.port_speeds_builder import PortSpeedsBuilder


class DeviceLinksBuilder:
    """
    Builds and executes requests for operations under /multicloud/interconnect/connectivity/device-links
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_interconnect_device_links(
        self,
        device_link_name: Optional[str] = None,
        interconnect_type: Optional[InterconnectTypeParam] = None,
        refresh: Optional[str] = "false",
        **kw,
    ) -> InterconnectDeviceLink:
        """
        API to retrieve Interconnect provider Device-Link.

        :param device_link_name: Interconnect Device Link name
        :param interconnect_type: Interconnect Provider Type
        :param refresh: Retrieve Interconnect Device-Link from provider enabled
        :returns: InterconnectDeviceLink
        """
        params = {
            "device-link-name": device_link_name,
            "interconnect-type": interconnect_type,
            "refresh": refresh,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/connectivity/device-links",
            return_type=InterconnectDeviceLink,
            params=params,
            **kw,
        )

    @property
    def add_interconnect_device_link(self):
        class add_interconnect_device_link_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[InterconnectDeviceLink] = None, **kw) -> ProcessResponse:
                """
                API to create a Device-Link in vManage.

                :param payload: Request Payload for Multicloud Interconnect Device Links
                :returns: ProcessResponse
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/interconnect/connectivity/device-links",
                    return_type=ProcessResponse,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectDeviceLink:
                return InterconnectDeviceLink(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectDeviceLink]:
                return InterconnectDeviceLink

        return add_interconnect_device_link_(self._request_adapter)

    def get_interconnect_device_link(self, device_link_name: str, **kw) -> InterconnectDeviceLink:
        """
        API to retrieve Interconnect provider Device-Link.

        :param device_link_name: Interconnect Device Link name
        :returns: InterconnectDeviceLink
        """
        params = {
            "device-link-name": device_link_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}",
            return_type=InterconnectDeviceLink,
            params=params,
            **kw,
        )

    @property
    def update_interconnect_device_link(self):
        class update_interconnect_device_link_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, device_link_name: str, payload: Optional[InterconnectDeviceLink] = None, **kw
            ) -> ProcessResponse:
                """
                API to update a Device-Link in vManage.

                :param device_link_name: Interconnect Device Link name
                :param payload: Request Payload for Multicloud Interconnect Device Links
                :returns: ProcessResponse
                """
                params = {
                    "device-link-name": device_link_name,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}",
                    return_type=ProcessResponse,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> InterconnectDeviceLink:
                return InterconnectDeviceLink(*args, **kwargs)

            @property
            def payload_model(self) -> Type[InterconnectDeviceLink]:
                return InterconnectDeviceLink

        return update_interconnect_device_link_(self._request_adapter)

    def delete_interconnect_device_link(self, device_link_name: str, **kw):
        """
        API to Delete Interconnect provider Device-Link.

        :param device_link_name: Interconnect Device Link name
        :returns: None
        """
        params = {
            "device-link-name": device_link_name,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}",
            params=params,
            **kw,
        )

    @property
    def metro_speed(self) -> MetroSpeedBuilder:
        """
        The metro-speed property
        """
        from .metro_speed.metro_speed_builder import MetroSpeedBuilder

        return MetroSpeedBuilder(self._request_adapter)

    @property
    def port_speeds(self) -> PortSpeedsBuilder:
        """
        The port-speeds property
        """
        from .port_speeds.port_speeds_builder import PortSpeedsBuilder

        return PortSpeedsBuilder(self._request_adapter)
