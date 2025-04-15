=========================
device.compliance.summary
=========================


Operation: GET /dataservice/device/compliance/summary
-----------------------------------------------------


Get compliance summary for devices

.. code:: python

    def get() -> DeviceComplianceSummaryResponse: ...


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
        client.device.compliance.summary.get()


.. toctree::
    :maxdepth: 1

    models

