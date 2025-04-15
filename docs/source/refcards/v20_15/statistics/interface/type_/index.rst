==========================
statistics.interface.type_
==========================


Operation: GET /dataservice/statistics/interface/type
-----------------------------------------------------


Get statistics per interface

.. code:: python

    def get(query: str) -> InterfaceAggResp: ...


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
        client.statistics.interface.type_.get()


.. toctree::
    :maxdepth: 1

    models

