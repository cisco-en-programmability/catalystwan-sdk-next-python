========================
data.device.state.fields
========================


Operation: GET /dataservice/data/device/state/{state_data_type}/fields
----------------------------------------------------------------------


Get device state data fileds

.. code:: python

    def generate_device_state_data_fields(
        state_data_type: str,
    ) -> List[GenerateDeviceStateDataFieldsInner]: ...


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
        client.data.device.state.fields.generate_device_state_data_fields()


.. toctree::
    :maxdepth: 1

    models

