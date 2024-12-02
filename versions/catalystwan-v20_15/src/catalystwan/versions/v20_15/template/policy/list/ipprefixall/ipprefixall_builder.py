# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .filtered.filtered_builder import FilteredBuilder
    from .preview.preview_builder import PreviewBuilder


class IpprefixallBuilder:
    """
    Builds and executes requests for operations under /template/policy/list/ipprefixall
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_lists_for_all_prefixes(self, **kw) -> List[Any]:
        """
        Get lists for all prefixes

        :returns: List[Any]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/list/ipprefixall",
            return_type=List[Any],
            **kw,
        )

    @property
    def create_policy_list_21(self):
        class create_policy_list_21_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create policy list

                :param payload: Policy list
                :returns: Any
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/template/policy/list/ipprefixall",
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_policy_list_21_(self._request_adapter)

    def delete_policy_lists_with_info_tag_21(
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
            "/dataservice/template/policy/list/ipprefixall",
            return_type=List[Any],
            params=params,
            **kw,
        )

    def get_lists_by_id_21(self, id: str, **kw) -> Any:
        """
        Get a specific policy list based on the id

        :param id: Policy Id
        :returns: Any
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/policy/list/ipprefixall/{id}",
            params=params,
            **kw,
        )

    @property
    def edit_policy_list_21(self):
        class edit_policy_list_21_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
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
                    "/dataservice/template/policy/list/ipprefixall/{id}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_policy_list_21_(self._request_adapter)

    def delete_policy_list_21(self, id: str, **kw):
        """
        Delete policy list entry for a specific type of policy list

        :param id: Policy Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/template/policy/list/ipprefixall/{id}",
            params=params,
            **kw,
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
