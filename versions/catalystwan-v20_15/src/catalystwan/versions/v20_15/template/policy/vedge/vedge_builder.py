# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .definition.definition_builder import DefinitionBuilder
    from .devices.devices_builder import DevicesBuilder


class VedgeBuilder:
    """
    Builds and executes requests for operations under /template/policy/vedge
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_policy_template_list(self, **kw) -> Any:
        """
        Get policy details

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/vedge", **kw
        )

    @property
    def create_v_edge_template(self):
        class create_v_edge_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create template

                :param payload: Template policy
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/template/policy/vedge", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_v_edge_template_(self._request_adapter)

    @property
    def edit_v_edge_template(self):
        class edit_v_edge_template_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, policy_id: str, payload: Optional[Any] = None, **kw
            ) -> Any:
                """
                Edit template

                :param policy_id: Policy Id
                :param payload: Template policy
                :returns: Any
                """
                params = {
                    "policyId": policy_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/policy/vedge/{policyId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_v_edge_template_(self._request_adapter)

    def delete_v_edge_template(self, policy_id: str, **kw):
        """
        Delete template

        :param policy_id: Policy Id
        :returns: None
        """
        params = {
            "policyId": policy_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/template/policy/vedge/{policyId}",
            params=params,
            **kw,
        )

    def change_policy_resource_group(
        self, policy_id: str, resource_group_name: str, **kw
    ):
        """
        Change policy resource group

        :param policy_id: Policy Id
        :param resource_group_name: Resrouce group name
        :returns: None
        """
        params = {
            "policyId": policy_id,
            "resourceGroupName": resource_group_name,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/template/policy/vedge/{resourceGroupName}/{policyId}",
            params=params,
            **kw,
        )

    @property
    def definition(self) -> DefinitionBuilder:
        """
        The definition property
        """
        from .definition.definition_builder import DefinitionBuilder

        return DefinitionBuilder(self._request_adapter)

    @property
    def devices(self) -> DevicesBuilder:
        """
        The devices property
        """
        from .devices.devices_builder import DevicesBuilder

        return DevicesBuilder(self._request_adapter)
