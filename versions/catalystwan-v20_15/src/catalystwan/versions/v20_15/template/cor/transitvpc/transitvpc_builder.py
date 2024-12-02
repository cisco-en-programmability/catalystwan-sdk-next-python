# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .autoscale_properties.autoscale_properties_builder import AutoscalePropertiesBuilder
    from .size.size_builder import SizeBuilder


class TransitvpcBuilder:
    """
    Builds and executes requests for operations under /template/cor/transitvpc
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_transit_vp_cs(
        self, accountid: str, cloudregion: str, cloudtype: Optional[str] = "AWS", **kw
    ) -> List[Any]:
        """
        Get transit VPC/VNet list

        :param accountid: Account Id
        :param cloudregion: Cloud region
        :param cloudtype: Cloud type
        :returns: List[Any]
        """
        logging.warning("Operation: %s is deprecated", "getTransitVPCs")
        params = {
            "accountid": accountid,
            "cloudregion": cloudregion,
            "cloudtype": cloudtype,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/cor/transitvpc",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def update_transit_vpc(self):
        class update_transit_vpc_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Update transit VPC/VNet

                :param payload: VPC
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "updateTransitVPC")
                return self._request_adapter.request(
                    "PUT", "/dataservice/template/cor/transitvpc", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_transit_vpc_(self._request_adapter)

    @property
    def add_transit_vpc(self):
        class add_transit_vpc_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create transit VPC/VNet

                :param payload: VPC
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "addTransitVPC")
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/cor/transitvpc",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return add_transit_vpc_(self._request_adapter)

    @property
    def autoscale_properties(self) -> AutoscalePropertiesBuilder:
        """
        The autoscale-properties property
        """
        from .autoscale_properties.autoscale_properties_builder import AutoscalePropertiesBuilder

        return AutoscalePropertiesBuilder(self._request_adapter)

    @property
    def size(self) -> SizeBuilder:
        """
        The size property
        """
        from .size.size_builder import SizeBuilder

        return SizeBuilder(self._request_adapter)
