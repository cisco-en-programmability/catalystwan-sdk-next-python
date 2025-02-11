================================
multicloud.settings.edge.global_
================================


Operation: GET /dataservice/multicloud/settings/edge/global
-----------------------------------------------------------


Deprecated!!!

Get edge global settings

.. code:: python

    def get_edge_global_settings(edge_type: EdgeTypeParam) -> Any: ...


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
        client.multicloud.settings.edge.global_.get_edge_global_settings()


Operation: PUT /dataservice/multicloud/settings/edge/global
-----------------------------------------------------------


Deprecated!!!

Update edge global settings for Edge provider

.. code:: python

    def update_edge_global_settings(
        payload: Optional[Any] = None,
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
        client.multicloud.settings.edge.global_.update_edge_global_settings()


Operation: POST /dataservice/multicloud/settings/edge/global
------------------------------------------------------------


Deprecated!!!

Add global settings for Edge provider

.. code:: python

    def add_edge_global_settings(
        payload: Optional[Any] = None,
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
        client.multicloud.settings.edge.global_.add_edge_global_settings()


.. toctree::
    :maxdepth: 1

    models

