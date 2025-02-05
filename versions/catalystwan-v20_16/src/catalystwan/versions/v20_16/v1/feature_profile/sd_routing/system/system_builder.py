# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .aaa.aaa_builder import AaaBuilder
    from .banner.banner_builder import BannerBuilder
    from .certificate.certificate_builder import CertificateBuilder
    from .flexible_port_speed.flexible_port_speed_builder import FlexiblePortSpeedBuilder
    from .global_.global_builder import GlobalBuilder
    from .logging.logging_builder import LoggingBuilder
    from .ntp.ntp_builder import NtpBuilder
    from .snmp.snmp_builder import SnmpBuilder


class SystemBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sd-routing/system
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdrouting_system_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SD-Routing System Feature Profiles

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sd-routing/system", params=params, **kw
        )

    def create_sdrouting_system_feature_profile(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a SD-Routing System Feature Profile

        :param payload: SD-Routing System Feature Profile
        :returns: str
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/v1/feature-profile/sd-routing/system",
            return_type=str,
            payload=payload,
            **kw,
        )

    def get_sdrouting_system_feature_profile(self, system_id: str, **kw) -> Any:
        """
        Get a SD-Routing System Feature Profile

        :param system_id: System Profile Id
        :returns: Any
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}",
            params=params,
            **kw,
        )

    def edit_sdrouting_system_feature_profile(
        self, system_id: str, payload: Optional[str] = None, **kw
    ) -> str:
        """
        Edit a SD-Routing System Feature Profile

        :param system_id: System Profile Id
        :param payload: SD-Routing System Feature Profile
        :returns: str
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_sdrouting_system_feature_profile(self, system_id: str, **kw):
        """
        Delete a SD-Routing System Feature Profile

        :param system_id: System Profile Id
        :returns: None
        """
        params = {
            "systemId": system_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sd-routing/system/{systemId}",
            params=params,
            **kw,
        )

    @property
    def aaa(self) -> AaaBuilder:
        """
        The aaa property
        """
        from .aaa.aaa_builder import AaaBuilder

        return AaaBuilder(self._request_adapter)

    @property
    def banner(self) -> BannerBuilder:
        """
        The banner property
        """
        from .banner.banner_builder import BannerBuilder

        return BannerBuilder(self._request_adapter)

    @property
    def certificate(self) -> CertificateBuilder:
        """
        The certificate property
        """
        from .certificate.certificate_builder import CertificateBuilder

        return CertificateBuilder(self._request_adapter)

    @property
    def flexible_port_speed(self) -> FlexiblePortSpeedBuilder:
        """
        The flexible-port-speed property
        """
        from .flexible_port_speed.flexible_port_speed_builder import FlexiblePortSpeedBuilder

        return FlexiblePortSpeedBuilder(self._request_adapter)

    @property
    def global_(self) -> GlobalBuilder:
        """
        The global property
        """
        from .global_.global_builder import GlobalBuilder

        return GlobalBuilder(self._request_adapter)

    @property
    def logging(self) -> LoggingBuilder:
        """
        The logging property
        """
        from .logging.logging_builder import LoggingBuilder

        return LoggingBuilder(self._request_adapter)

    @property
    def ntp(self) -> NtpBuilder:
        """
        The ntp property
        """
        from .ntp.ntp_builder import NtpBuilder

        return NtpBuilder(self._request_adapter)

    @property
    def snmp(self) -> SnmpBuilder:
        """
        The snmp property
        """
        from .snmp.snmp_builder import SnmpBuilder

        return SnmpBuilder(self._request_adapter)
