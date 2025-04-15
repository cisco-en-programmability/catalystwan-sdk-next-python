=====================
dca.data.device.state
=====================


Operation: POST /dataservice/dca/data/device/state/{state_data_type}
--------------------------------------------------------------------


Get device state data

.. code:: python

    def post(state_data_type: str, payload: Any) -> Any: ...


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
        client.dca.data.device.state.post()


