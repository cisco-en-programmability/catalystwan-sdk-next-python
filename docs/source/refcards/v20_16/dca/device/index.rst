==========
dca.device
==========


Operation: POST /dataservice/dca/device
---------------------------------------


Get all devices

.. code:: python

    def list_all_devices_dca(
        payload: Optional[Any] = None,
    ) -> List[Any]: ...


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
        client.dca.device.list_all_devices_dca()


.. toctree::
    :maxdepth: 1

    crashlog/index

