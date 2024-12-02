# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .async_.async_builder import AsyncBuilder
    from .bulk.bulk_builder import BulkBuilder
    from .vsmart.vsmart_builder import VsmartBuilder
    from .vsmart_mt.vsmart_mt_builder import VsmartMtBuilder
    from .delete.delete_builder import DeleteBuilder
    from .switch.switch_builder import SwitchBuilder
    from .vsessionid.vsessionid_builder import VsessionidBuilder


class TenantBuilder:
    """
    Builds and executes requests for operations under /tenant
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_all_tenants(self, device_id: Optional[str] = None, **kw) -> List[Any]:
        """
        Lists all the tenants on the vManage


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param device_id: List all tenants associated with a vSmart or MTEdge
        :returns: List[Any]
        """
        params = {
            "deviceId": device_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/tenant", return_type=List[Any], params=params, **kw
        )

    @property
    def create_tenant(self):
        class create_tenant_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create a new tenant in Multi-Tenant vManage


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param payload: Tenant model
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/tenant", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_tenant_(self._request_adapter)

    def get_tenant(self, tenant_id: str, **kw) -> Any:
        """
        Get a tenant by Id


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param tenant_id: Tenant Id
        :returns: Any
        """
        params = {
            "tenantId": tenant_id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/tenant/{tenantId}", params=params, **kw
        )

    @property
    def update_tenant(self):
        class update_tenant_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, tenant_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Update a tenant in Multi-Tenant vManage


                Note: In a multitenant vManage system, this API is only available in the Provider view.

                :param tenant_id: Tenant Id
                :param payload: Tenant model
                :returns: Any
                """
                params = {
                    "tenantId": tenant_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/tenant/{tenantId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_tenant_(self._request_adapter)

    @property
    def async_(self) -> AsyncBuilder:
        """
        The async property
        """
        from .async_.async_builder import AsyncBuilder

        return AsyncBuilder(self._request_adapter)

    @property
    def bulk(self) -> BulkBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_builder import BulkBuilder

        return BulkBuilder(self._request_adapter)

    @property
    def delete(self) -> DeleteBuilder:
        """
        The delete property
        """
        from .delete.delete_builder import DeleteBuilder

        return DeleteBuilder(self._request_adapter)

    @property
    def switch(self) -> SwitchBuilder:
        """
        The switch property
        """
        from .switch.switch_builder import SwitchBuilder

        return SwitchBuilder(self._request_adapter)

    @property
    def vsessionid(self) -> VsessionidBuilder:
        """
        The vsessionid property
        """
        from .vsessionid.vsessionid_builder import VsessionidBuilder

        return VsessionidBuilder(self._request_adapter)

    @property
    def vsmart(self) -> VsmartBuilder:
        """
        The vsmart property
        """
        from .vsmart.vsmart_builder import VsmartBuilder

        return VsmartBuilder(self._request_adapter)

    @property
    def vsmart_mt(self) -> VsmartMtBuilder:
        """
        The vsmart-mt property
        """
        from .vsmart_mt.vsmart_mt_builder import VsmartMtBuilder

        return VsmartMtBuilder(self._request_adapter)
