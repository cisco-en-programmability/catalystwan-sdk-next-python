================================
multicloud.settings.edge.global_
================================


Operation: GET /dataservice/multicloud/settings/edge/global
-----------------------------------------------------------


Deprecated!!!

Get edge global settings

.. code:: python

    def get(edge_type: EdgeTypeParam) -> Any: ...


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
        client.multicloud.settings.edge.global_.get()


Operation: PUT /dataservice/multicloud/settings/edge/global
-----------------------------------------------------------


Deprecated!!!

Update edge global settings for Edge provider

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.multicloud.settings.edge.global_.put()


Operation: POST /dataservice/multicloud/settings/edge/global
------------------------------------------------------------


Deprecated!!!

Add global settings for Edge provider

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.multicloud.settings.edge.global_.post()


.. toctree::
    :maxdepth: 1

    models

