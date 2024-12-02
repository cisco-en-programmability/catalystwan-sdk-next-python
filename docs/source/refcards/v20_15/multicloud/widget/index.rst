=================
multicloud.widget
=================


Operation: GET /dataservice/multicloud/widget
---------------------------------------------


Get All cloud widgets

.. code:: python

    def get_all_cloud_widgets() -> List[CloudWidget]: ...


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
        client.multicloud.widget.get_all_cloud_widgets()


Operation: GET /dataservice/multicloud/widget/{cloudType}
---------------------------------------------------------


Get cloud widget by cloud type

.. code:: python

    def get_cloud_widget(cloud_type: str) -> CloudWidget: ...


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
        client.multicloud.widget.get_cloud_widget()


.. toctree::
    :maxdepth: 1

    edge
    models

