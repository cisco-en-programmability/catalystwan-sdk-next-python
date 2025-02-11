=============================
data.device.statistics.fields
=============================


Operation: GET /dataservice/data/device/statistics/{state_data_type}/fields
---------------------------------------------------------------------------


Get statistics fields and types

.. code:: python

    def get_stat_data_fields_by_state_data_type(
        state_data_type: str,
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
        client.data.device.statistics.fields.get_stat_data_fields_by_state_data_type()


