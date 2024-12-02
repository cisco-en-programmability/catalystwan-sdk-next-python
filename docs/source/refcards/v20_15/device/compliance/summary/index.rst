=========================
device.compliance.summary
=========================


Operation: GET /dataservice/device/compliance/summary
-----------------------------------------------------


Get compliance summary for devices

.. code:: python

    def get_compliance_summary() -> DeviceComplianceSummaryResponse: ...


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
        client.device.compliance.summary.get_compliance_summary()


.. toctree::
    :maxdepth: 1

    models

