# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .bulk.bulk_builder import BulkBuilder
    from .multiple.multiple_builder import MultipleBuilder
    from .preview.preview_builder import PreviewBuilder


class FxsportBuilder:
    """
    Builds and executes requests for operations under /template/policy/definition/fxsport
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_definitions_27(self, **kw) -> Any:
        """
        Get policy definitions

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/definition/fxsport", **kw
        )

    def create_policy_definition_27(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create policy definition

        :param payload: Policy definition
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/definition/fxsport", payload=payload, **kw
        )

    def get_policy_definition_27(self, id: str, **kw) -> Any:
        """
        Get a specific policy definitions

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/definition/fxsport/{id}", params=params, **kw
        )

    def edit_policy_definition_27(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
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
            "/dataservice/template/policy/definition/fxsport/{id}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_policy_definition_27(self, id: str, **kw):
        """
        Delete policy definition

        :param id: Policy Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/definition/fxsport/{id}", params=params, **kw
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
