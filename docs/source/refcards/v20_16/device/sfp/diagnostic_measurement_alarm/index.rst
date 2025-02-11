=======================================
device.sfp.diagnostic_measurement_alarm
=======================================


Operation: GET /dataservice/device/sfp/diagnosticMeasurementAlarm
-----------------------------------------------------------------


Get SFP diagnostic measurement alarm

.. code:: python

    def get_diagnostic_measurement_alarm(
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
        client.device.sfp.diagnostic_measurement_alarm.get_diagnostic_measurement_alarm()


.. toctree::
    :maxdepth: 1

    models

