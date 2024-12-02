# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .bulk.bulk_builder import BulkBuilder
    from .multiple.multiple_builder import MultipleBuilder
    from .preview.preview_builder import PreviewBuilder


class IntrusionpreventionBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/intrusionprevention
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_definitions_18(self, **kw) -> Any:
        """
        Get policy definitions

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/definition/intrusionprevention", **kw
        )

    @property
    def create_policy_definition_18(self):
        class create_policy_definition_18_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create policy definition

                :param payload: Policy definition
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/definition/intrusionprevention",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_policy_definition_18_(self._request_adapter)

    def get_policy_definition_18(self, id: str, **kw) -> Any:
        """
        Get a specific policy definitions

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/definition/intrusionprevention/{id}",
            params=params,
            **kw,
        )

    @property
    def edit_policy_definition_18(self):
        class edit_policy_definition_18_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
                """
                Edit a policy definitions

                :param id: Policy Id
                :param payload: Policy definition
                :returns: Any
                """
                params = {
                    "id": id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/template/policy/definition/intrusionprevention/{id}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_policy_definition_18_(self._request_adapter)

    def delete_policy_definition_18(self, id: str, **kw):
        """
        Delete policy definition

        :param id: Policy Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/template/policy/definition/intrusionprevention/{id}",
            params=params,
            **kw,
        )

    @property
    def bulk(self) -> BulkBuilder:
        """
        The bulk property
        """
        from .bulk.bulk_builder import BulkBuilder

        return BulkBuilder(self._request_adapter)

    @property
    def multiple(self) -> MultipleBuilder:
        """
        The multiple property
        """
        from .multiple.multiple_builder import MultipleBuilder

        return MultipleBuilder(self._request_adapter)

    @property
    def preview(self) -> PreviewBuilder:
        """
        The preview property
        """
        from .preview.preview_builder import PreviewBuilder

        return PreviewBuilder(self._request_adapter)
