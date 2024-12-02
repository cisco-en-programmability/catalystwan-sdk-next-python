# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import HostVpcTagPost, HostVpcTagPut, HostVpcTagResponse, Taskid

if TYPE_CHECKING:
    from .rebalance_vnets.rebalance_vnets_builder import RebalanceVnetsBuilder


class TagsBuilder:
    """
    Builds and executes requests for operations under /multicloud/hostvpc/tags
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_vpc_tags(
        self,
        cloud_type: Optional[str] = None,
        region: Optional[str] = None,
        tag_name: Optional[str] = None,
        **kw,
    ) -> List[HostVpcTagResponse]:
        """
        Get VPC Tags

        :param cloud_type: Multicloud provider type
        :param region: Region
        :param tag_name: Tag name
        :returns: List[HostVpcTagResponse]
        """
        params = {
            "cloudType": cloud_type,
            "region": region,
            "tagName": tag_name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/multicloud/hostvpc/tags",
            return_type=List[HostVpcTagResponse],
            params=params,
            **kw,
        )

    @property
    def edit_tag(self):
        class edit_tag_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[HostVpcTagPut] = None, **kw) -> Taskid:
                """
                Edit VPCs for a Tag

                :param payload: Payload for updating VPCs for a Tag
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/multicloud/hostvpc/tags",
                    return_type=Taskid,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> HostVpcTagPut:
                return HostVpcTagPut(*args, **kwargs)

            @property
            def payload_model(self) -> Type[HostVpcTagPut]:
                return HostVpcTagPut

        return edit_tag_(self._request_adapter)

    @property
    def host_vpc_tagging(self):
        class host_vpc_tagging_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, payload: Optional[HostVpcTagPost] = None, **kw
            ) -> Taskid:
                """
                Tag a VPC

                :param payload: Payload for tagging a VPC
                :returns: Taskid
                """
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/multicloud/hostvpc/tags",
                    return_type=Taskid,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> HostVpcTagPost:
                return HostVpcTagPost(*args, **kwargs)

            @property
            def payload_model(self) -> Type[HostVpcTagPost]:
                return HostVpcTagPost

        return host_vpc_tagging_(self._request_adapter)

    def un_tag(self, tag_name: str, **kw) -> Taskid:
        """
        Delete a Tag

        :param tag_name: Tag name
        :returns: Taskid
        """
        params = {
            "tagName": tag_name,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/multicloud/hostvpc/tags/{tagName}",
            return_type=Taskid,
            params=params,
            **kw,
        )

    @property
    def rebalance_vnets(self) -> RebalanceVnetsBuilder:
        """
        The rebalanceVnets property
        """
        from .rebalance_vnets.rebalance_vnets_builder import RebalanceVnetsBuilder

        return RebalanceVnetsBuilder(self._request_adapter)
