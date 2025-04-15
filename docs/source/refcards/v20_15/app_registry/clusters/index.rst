=====================
app_registry.clusters
=====================


Operation: GET /dataservice/app-registry/clusters
-------------------------------------------------


Obtain all clusters with associated cloud accounts

.. code:: python

    def get(
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
        client.app_registry.clusters.get()


Operation: POST /dataservice/app-registry/clusters
--------------------------------------------------


Manually upload kubeConfig

.. code:: python

    def post() -> None: ...


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
        client.app_registry.clusters.post()


Operation: PUT /dataservice/app-registry/clusters/{id}
------------------------------------------------------


Edit the discovery status of a cluster

.. code:: python

    def put(id: str, payload: PutProperties) -> None: ...


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
        client.app_registry.clusters.put()


Operation: DELETE /dataservice/app-registry/clusters/{id}
---------------------------------------------------------


Delete manually uploaded cluster

.. code:: python

    def delete(id: str) -> None: ...


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
        client.app_registry.clusters.delete()


.. toctree::
    :maxdepth: 1

    models

