=================
data.device.state
=================


Operation: GET /dataservice/data/device/state/{state_data_type}
---------------------------------------------------------------


Get device state data

.. code:: python

    def generate_device_state_data(
        state_data_type: str,
        start_id: Optional[str] = None,
        count: Optional[int] = 1000,
    ) -> GenerateDeviceStateData: ...


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
        client.data.device.state.generate_device_state_data()


.. toctree::
    :maxdepth: 1

    fields/index
    query/index
    models

