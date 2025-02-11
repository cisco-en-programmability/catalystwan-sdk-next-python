=====================
app_registry.clusters
=====================


Operation: GET /dataservice/app-registry/clusters
-------------------------------------------------


Obtain all clusters with associated cloud accounts

.. code:: python

    def get_kubernetes_cluster(
        is_cached: Optional[bool] = True,
        offset: Optional[int] = 0,
        limit: Optional[int] = 0,
    ) -> List[ClusterProperties]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.app_registry.clusters.get_kubernetes_cluster()


Operation: POST /dataservice/app-registry/clusters
--------------------------------------------------


Manually upload kubeConfig

.. code:: python

    def post_cluster() -> None: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.app_registry.clusters.post_cluster()


Operation: PUT /dataservice/app-registry/clusters/{id}
------------------------------------------------------


Edit the discovery status of a cluster

.. code:: python

    def edit_kubernetes_cluster(
        id: str, payload: Optional[PutProperties] = None
    ) -> None: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.app_registry.clusters.edit_kubernetes_cluster()


Operation: DELETE /dataservice/app-registry/clusters/{id}
---------------------------------------------------------


Delete manually uploaded cluster

.. code:: python

    def delete_kubernetes_cluster(id: str) -> None: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.app_registry.clusters.delete_kubernetes_cluster()


.. toctree::
    :maxdepth: 1

    models

