# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, List, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import GetMapResponse
from .models import CloudTypeParam
from .models import Taskid
from .models import PostMapRequest

if TYPE_CHECKING:
    from .defaults.defaults_builder import DefaultsBuilder
    from .status.status_builder import StatusBuilder
    from .summary.summary_builder import SummaryBuilder
    from .tags.tags_builder import TagsBuilder
    from .vpns.vpns_builder import VpnsBuilder


class MapBuilder:
    """
    Builds and executes requests for operations under /multicloud/map
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_mapping_matrix(
        self, cloud_type: CloudTypeParam, **kw
    ) -> List[GetMapResponse]:
        """
        Get Mapping details for cloudType

        :param cloud_type: Cloud type
        :returns: List[GetMapResponse]
        """
        params = {
            "cloudType": cloud_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/map",
            return_type=List[GetMapResponse],
            params=params,
            **kw,
        )

    @property
    def process_mapping(self):
        class process_mapping_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[PostMapRequest] = None, **kw
            ) -> Taskid:
                """
                Enable Mapping for cloudType

                :param payload: Payloads for enable mapping
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/map",
                    return_type=Taskid,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> PostMapRequest:
                return PostMapRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PostMapRequest]:
                return PostMapRequest

        return process_mapping_(self._request_adapter)

    @property
    def defaults(self) -> DefaultsBuilder:
        """
        The defaults property
        """
        from .defaults.defaults_builder import DefaultsBuilder

        return DefaultsBuilder(self._request_adapter)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)

    @property
    def summary(self) -> SummaryBuilder:
        """
        The summary property
        """
        from .summary.summary_builder import SummaryBuilder

        return SummaryBuilder(self._request_adapter)

    @property
    def tags(self) -> TagsBuilder:
        """
        The tags property
        """
        from .tags.tags_builder import TagsBuilder

        return TagsBuilder(self._request_adapter)

    @property
    def vpns(self) -> VpnsBuilder:
        """
        The vpns property
        """
        from .vpns.vpns_builder import VpnsBuilder

        return VpnsBuilder(self._request_adapter)
