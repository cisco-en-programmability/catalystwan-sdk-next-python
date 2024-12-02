====================================================
v2.data.device.statistics.interfacestatistics.fields
====================================================


Operation: GET /dataservice/v2/data/device/statistics/interfacestatistics/fields
--------------------------------------------------------------------------------


Get statistics fields and types

.. code:: python

    def get_stat_data_fields_by_interface_statistics() -> List[Field]: ...


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
        client.v2.data.device.statistics.interfacestatistics.fields.get_stat_data_fields_by_interface_statistics()


.. toctree::
    :maxdepth: 1

    models

