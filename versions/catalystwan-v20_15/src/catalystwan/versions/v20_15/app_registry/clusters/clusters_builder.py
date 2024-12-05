# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import List, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import ClusterProperties, PutProperties


class ClustersBuilder:
    """
    Builds and executes requests for operations under /app-registry/clusters
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_kubernetes_cluster(
        self, is_cached: Optional[bool] = True, offset: Optional[int] = 0, limit: Optional[int] = 0, **kw
    ) -> List[ClusterProperties]:
        """
        Obtain all clusters with associated cloud accounts

        :param is_cached: Is cached
        :param offset: Pagination offset
        :param limit: Pagination limit
        :returns: List[ClusterProperties]
        """
        params = {
            "isCached": is_cached,
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/app-registry/clusters", return_type=List[ClusterProperties], params=params, **kw
        )

    def post_cluster(self, **kw):
        """
        Manually upload kubeConfig

        :returns: None
        """
        return self._request_adapter.request("POST", "/dataservice/app-registry/clusters", **kw)

    @property
    def edit_kubernetes_cluster(self):
        class edit_kubernetes_cluster_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[PutProperties] = None, **kw):
                """
                Edit the discovery status of a cluster

                :param id: Id
                :param payload: enable or disable Cluster Discovery Status
                :returns: None
                """
                params = {
                    "id": id,
                }
                return self._request_adapter.request(
                    "PUT", "/dataservice/app-registry/clusters/{id}", params=params, payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> PutProperties:
                return PutProperties(*args, **kwargs)

            @property
            def payload_model(self) -> Type[PutProperties]:
                return PutProperties

        return edit_kubernetes_cluster_(self._request_adapter)

    def delete_kubernetes_cluster(self, id: str, **kw):
        """
        Delete manually uploaded cluster

        :param id: Id
        :returns: None
        """
        params = {
            "id": id,
        }
        return self._request_adapter.request("DELETE", "/dataservice/app-registry/clusters/{id}", params=params, **kw)
