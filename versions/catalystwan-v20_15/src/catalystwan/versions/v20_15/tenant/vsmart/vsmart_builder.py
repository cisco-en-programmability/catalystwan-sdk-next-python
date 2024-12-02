# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .capacity.capacity_builder import CapacityBuilder


class VsmartBuilder:
    """
    Builds and executes requests for operations under /tenant/vsmart
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_tenantv_smart_mapping(self, **kw) -> List[Any]:
        """
        Retrieve mapping of tenants to vSmarts


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/tenant/vsmart", return_type=List[Any], **kw
        )

    @property
    def update_tenantv_smart_placement(self):
        class update_tenantv_smart_placement_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, tenant_id: str, payload: Optional[Any] = None, **kw
            ) -> List[Any]:
                """
                Update placement of the Tenant from source vSmart to destination vSmart


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param tenant_id: Tenant Id
                :param payload: Tenant model
                :returns: List[Any]
                """
                params = {
                    "tenantId": tenant_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/tenant/{tenantId}/vsmart",
                    return_type=List[Any],
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_tenantv_smart_placement_(self._request_adapter)

    @property
    def capacity(self) -> CapacityBuilder:
        """
        The capacity property
        """
        from .capacity.capacity_builder import CapacityBuilder

        return CapacityBuilder(self._request_adapter)
