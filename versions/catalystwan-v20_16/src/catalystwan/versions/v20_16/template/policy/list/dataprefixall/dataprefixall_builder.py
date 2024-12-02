# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .filtered.filtered_builder import FilteredBuilder
    from .preview.preview_builder import PreviewBuilder


class DataprefixallBuilder:
    """
    Builds and executes requests for operations under /template/policy/list/dataprefixall
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lists_for_all_data_prefixes(self, **kw) -> List[Any]:
        """
        Get policy lists for all data prefixes

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/list/dataprefixall", return_type=List[Any], **kw
        )

    def create_policy_list_9(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create policy list

        :param payload: Policy list
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/list/dataprefixall", payload=payload, **kw
        )

    def delete_policy_lists_with_info_tag_9(
        self, info_tag: Optional[str] = None, **kw
    ) -> List[Any]:
        """
        Delete policy lists with specific info tag

        :param info_tag: InfoTag
        :returns: List[Any]
        """
        params = {
            "infoTag": info_tag,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/template/policy/list/dataprefixall",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def get_lists_by_id_9(self, id: str, **kw) -> Any:
        """
        Get a specific policy list based on the id

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/list/dataprefixall/{id}", params=params, **kw
        )

    def edit_policy_list_9(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Edit policy list entries for a specific type of policy list

        :param id: Policy Id
        :param payload: Policy list
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/template/policy/list/dataprefixall/{id}",
            params=params,
            payload=payload,
            **kw,
        )

    def delete_policy_list_9(self, id: str, **kw):
        """
        Delete policy list entry for a specific type of policy list

        :param id: Policy Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/list/dataprefixall/{id}", params=params, **kw
        )

    @property
    def filtered(self) -> FilteredBuilder:
        """
        The filtered property
        """
        from .filtered.filtered_builder import FilteredBuilder

        return FilteredBuilder(self._request_adapter)

    @property
    def preview(self) -> PreviewBuilder:
        """
        The preview property
        """
        from .preview.preview_builder import PreviewBuilder

        return PreviewBuilder(self._request_adapter)
