# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .thousandeyes.thousandeyes_builder import ThousandeyesBuilder
    from .ucse.ucse_builder import UcseBuilder


class OtherBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/other
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sdwan_other_feature_profiles(
        self, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> Any:
        """
        Get all SDWAN Feature Profiles with giving Family and profile type

        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: Any
        """
        params = {
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/v1/feature-profile/sdwan/other", params=params, **kw
        )

    @property
    def create_sdwan_other_feature_profile(self):
        class create_sdwan_other_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[str] = None, **kw) -> str:
                """
                Create a SDWAN Other Feature Profile

                :param payload: SDWAN Feature profile
                :returns: str
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/other",
                    return_type=str,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_sdwan_other_feature_profile_(self._request_adapter)

    def get_sdwan_other_feature_profile_by_profile_id(self, other_id: str, **kw) -> Any:
        """
        Get a SDWAN Other Feature Profile with otherId

        :param other_id: Feature Profile Id
        :returns: Any
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}",
            params=params,
            **kw,
        )

    @property
    def edit_sdwan_other_feature_profile(self):
        class edit_sdwan_other_feature_profile_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, other_id: str, payload: Optional[str] = None, **kw
            ) -> str:
                """
                Edit a SDWAN Other Feature Profile

                :param other_id: Feature Profile Id
                :param payload: SDWAN Feature profile
                :returns: str
                """
                params = {
                    "otherId": other_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/other/{otherId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_sdwan_other_feature_profile_(self._request_adapter)

    def delete_sdwan_other_feature_profile(self, other_id: str, **kw):
        """
        Delete Feature Profile

        :param other_id: Other id
        :returns: None
        """
        params = {
            "otherId": other_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/other/{otherId}",
            params=params,
            **kw,
        )

    @property
    def thousandeyes(self) -> ThousandeyesBuilder:
        """
        The thousandeyes property
        """
        from .thousandeyes.thousandeyes_builder import ThousandeyesBuilder

        return ThousandeyesBuilder(self._request_adapter)

    @property
    def ucse(self) -> UcseBuilder:
        """
        The ucse property
        """
        from .ucse.ucse_builder import UcseBuilder

        return UcseBuilder(self._request_adapter)
