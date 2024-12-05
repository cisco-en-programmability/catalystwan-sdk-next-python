# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .filtered.filtered_builder import FilteredBuilder
    from .preview.preview_builder import PreviewBuilder


class Dataipv6PrefixBuilder:
    """
    Builds and executes requests for operations under /template/policy/list/dataipv6prefix
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_policy_lists_8(self, **kw) -> List[Any]:
        """
        Get policy lists

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/list/dataipv6prefix", return_type=List[Any], **kw
        )

    def create_policy_list_8(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create policy list

        :param payload: Policy list
        :returns: Any
        """
        return self._request_adapter.request(
            "POST", "/dataservice/template/policy/list/dataipv6prefix", payload=payload, **kw
        )

    def delete_policy_lists_with_info_tag_8(self, info_tag: Optional[str] = None, **kw) -> List[Any]:
        """
        Delete policy lists with specific info tag

        :param info_tag: InfoTag
        :returns: List[Any]
        """
        params = {
            "infoTag": info_tag,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/list/dataipv6prefix", return_type=List[Any], params=params, **kw
        )

    def get_lists_by_id_8(self, id: str, **kw) -> Any:
        """
        Get a specific policy list based on the id

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/policy/list/dataipv6prefix/{id}", params=params, **kw
        )

    def edit_policy_list_8(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
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
            "PUT", "/dataservice/template/policy/list/dataipv6prefix/{id}", params=params, payload=payload, **kw
        )

    def delete_policy_list_8(self, id: str, **kw):
        """
        Delete policy list entry for a specific type of policy list

        :param id: Policy Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/policy/list/dataipv6prefix/{id}", params=params, **kw
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
