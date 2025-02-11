=====================
dca.data.device.state
=====================


Operation: POST /dataservice/dca/data/device/state/{state_data_type}
--------------------------------------------------------------------


Get device state data

.. code:: python

    def generate_dca_device_state_data(
        state_data_type: str, payload: Optional[Any] = None
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
        client.dca.data.device.state.generate_dca_device_state_data()


