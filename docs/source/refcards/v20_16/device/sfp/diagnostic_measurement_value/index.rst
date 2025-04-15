=======================================
device.sfp.diagnostic_measurement_value
=======================================


Operation: GET /dataservice/device/sfp/diagnosticMeasurementValue
-----------------------------------------------------------------


Get SFP diagnostic measurement value

.. code:: python

    def get(
        device_id: str, ifname: Optional[IfnameParam] = None
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
        client.device.sfp.diagnostic_measurement_value.get()


.. toctree::
    :maxdepth: 1

    models

