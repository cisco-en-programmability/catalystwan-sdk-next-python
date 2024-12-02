=====================
device.pim.rp_mapping
=====================


Operation: GET /dataservice/device/pim/rp-mapping
-------------------------------------------------


Get PIM Rp-mapping list from device

.. code:: python

    def create_pim_rp_mapping_list(device_id: str) -> List[Any]: ...


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
        client.device.pim.rp_mapping.create_pim_rp_mapping_list()


