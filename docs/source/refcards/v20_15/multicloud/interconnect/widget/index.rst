==============================
multicloud.interconnect.widget
==============================


Operation: GET /dataservice/multicloud/interconnect/widget
----------------------------------------------------------


.. code:: python

    @overload
    def get() -> List[InterconnectWidget]: ...


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
        client.multicloud.interconnect.widget.get()


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/widget
------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(interconnect_type: str) -> InterconnectWidget: ...


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
        client.multicloud.interconnect.widget.get()


.. toctree::
    :maxdepth: 1

    models

