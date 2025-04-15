=======================
data.device.state.query
=======================


Operation: GET /dataservice/data/device/state/{state_data_type}/query
---------------------------------------------------------------------


Get device state data fileds

.. code:: python

    def get(
        state_data_type: str,
    ) -> GenerateDeviceStateDataWithQueryString: ...


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
        client.data.device.state.query.get()


.. toctree::
    :maxdepth: 1

    models

