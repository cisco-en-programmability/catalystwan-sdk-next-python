# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import (AttachSitesRequestPayloadInner, DetachSitesRequestPayloadInner, GetSitesResponse, Taskid,
                     TunnelScalingRequestPayload)


class SiteBuilder:
    """
    Builds and executes requests for operations under /multicloud/cloudgateway/{cloudGatewayName}/site
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_cgw_attached_sites(
        self,
        cloud_gateway_name: str,
        system_ip: Optional[str] = None,
        site_id: Optional[str] = None,
        color: Optional[str] = None,
        vpn_tunnel_status: Optional[str] = None,
        solution: Optional[str] = None,
        **kw,
    ) -> GetSitesResponse:
        """
        Get sites attached to CGW

        :param cloud_gateway_name: Name of Cloud Gateway to attach site
        :param system_ip: System Ip of Branch Device
        :param site_id: Site Id
        :param color: color
        :param vpn_tunnel_status: Tunnel status of device
        :param solution: Solution of branch device
        :returns: GetSitesResponse
        """
        params = {
            "cloudGatewayName": cloud_gateway_name,
            "systemIp": system_ip,
            "siteId": site_id,
            "color": color,
            "vpnTunnelStatus": vpn_tunnel_status,
            "solution": solution,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/cloudgateway/{cloudGatewayName}/site",
            return_type=GetSitesResponse,
            params=params,
            **kw,
        )

    @property
    def tunnel_scaling(self):
        class tunnel_scaling_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cloud_gateway_name: str, payload: Optional[TunnelScalingRequestPayload] = None, **kw
            ) -> Taskid:
                """
                Update tunnel scaling and accelerated vpn parameter for a branch endpoint

                :param cloud_gateway_name: Name of Cloud Gateway to attach site
                :param payload: Site Information
                :returns: Taskid
                """
                params = {
                    "cloudGatewayName": cloud_gateway_name,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/cloudgateway/{cloudGatewayName}/site",
                    return_type=Taskid,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> TunnelScalingRequestPayload:
                return TunnelScalingRequestPayload(*args, **kwargs)

            @property
            def payload_model(self) -> Type[TunnelScalingRequestPayload]:
                return TunnelScalingRequestPayload

        return tunnel_scaling_(self._request_adapter)

    @property
    def attach_sites(self):
        class attach_sites_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cloud_gateway_name: str, payload: Optional[List[AttachSitesRequestPayloadInner]] = None, **kw
            ) -> Taskid:
                """
                Attach sites to Cloud Gateway

                :param cloud_gateway_name: Name of Cloud Gateway to attach site
                :param payload: Site Information
                :returns: Taskid
                """
                params = {
                    "cloudGatewayName": cloud_gateway_name,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/cloudgateway/{cloudGatewayName}/site",
                    return_type=Taskid,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> List[AttachSitesRequestPayloadInner]:
                return List[AttachSitesRequestPayloadInner](*args, **kwargs)

            @property
            def payload_model(self) -> Type[List[AttachSitesRequestPayloadInner]]:
                return List[AttachSitesRequestPayloadInner]

        return attach_sites_(self._request_adapter)

    @property
    def detach_sites_1(self):
        class detach_sites_1_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, cloud_gateway_name: str, payload: Optional[List[DetachSitesRequestPayloadInner]] = None, **kw
            ) -> Taskid:
                """
                Detach sites from cloud gateway

                :param cloud_gateway_name: Name of Cloud Gateway to attach site
                :param payload: Site Information
                :returns: Taskid
                """
                params = {
                    "cloudGatewayName": cloud_gateway_name,
                }
                return self._request_adapter.request(
                    "DELETE",
                    "/dataservice/multicloud/cloudgateway/{cloudGatewayName}/site",
                    return_type=Taskid,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> List[DetachSitesRequestPayloadInner]:
                return List[DetachSitesRequestPayloadInner](*args, **kwargs)

            @property
            def payload_model(self) -> Type[List[DetachSitesRequestPayloadInner]]:
                return List[DetachSitesRequestPayloadInner]

        return detach_sites_1_(self._request_adapter)
