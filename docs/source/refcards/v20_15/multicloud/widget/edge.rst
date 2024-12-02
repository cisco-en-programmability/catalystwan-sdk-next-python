======================
multicloud.widget.edge
======================


Operation: GET /dataservice/multicloud/widget/edge
--------------------------------------------------


Deprecated!!!

Get All Interconnect Edge widgets

.. code:: python

    def get_all_edge_widgets() -> Any: ...


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
        client.multicloud.widget.edge.get_all_edge_widgets()


Operation: GET /dataservice/multicloud/widget/edge/{edgeType}
-------------------------------------------------------------


Deprecated!!!

Get Interconnect Edge widget by edge type

.. code:: python

    def get_edge_widget(edge_type: str) -> Any: ...


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
        client.multicloud.widget.edge.get_edge_widget()


