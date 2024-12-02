=================
device.compliance
=================


Operation: GET /dataservice/device/compliance
---------------------------------------------


Get compliance information for devices

.. code:: python

    def get_compliance_details(
        offset: Optional[int] = 0,
        limit: Optional[int] = 25,
        device_type: Optional[List[str]] = None,
        status: Optional[List[str]] = None,
        type_: Optional[List[str]] = None,
        sort_by: Optional[str] = None,
        order_by: Optional[OrderByParam] = None,
    ) -> DeviceComplianceApiResponse: ...


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
        client.device.compliance.get_compliance_details()


.. toctree::
    :maxdepth: 1

    summary/index
    models

