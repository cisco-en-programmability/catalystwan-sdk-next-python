===============
sig.datacenters
===============


Operation: GET /dataservice/sig/datacenters/{type}/{tunneltype}
---------------------------------------------------------------


The API to get all sig data center for given provider type

.. code:: python

    def get_sig_dynamic_data_center_list(
        type_: str, tunneltype: str
    ) -> GetDataCenters: ...


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
        client.sig.datacenters.get_sig_dynamic_data_center_list()


Operation: GET /dataservice/sig/datacenters/{type}/{tunneltype}/{devicetype}
----------------------------------------------------------------------------


Get list of data centers for zscaler or umbrella

.. code:: python

    def get_sig_data_center_list(
        type_: str, tunneltype: str, devicetype: str
    ) -> Any: ...


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
        client.sig.datacenters.get_sig_data_center_list()


.. toctree::
    :maxdepth: 1

    models

