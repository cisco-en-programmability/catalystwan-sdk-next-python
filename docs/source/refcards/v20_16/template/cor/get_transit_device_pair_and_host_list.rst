==================================================
template.cor.get_transit_device_pair_and_host_list
==================================================


Operation: GET /dataservice/template/cor/getTransitDevicePairAndHostList
------------------------------------------------------------------------


Deprecated!!!

Get device and host details

.. code:: python

    def get(account_id: str, cloud_region: str) -> Any: ...


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
        client.template.cor.get_transit_device_pair_and_host_list.get()


