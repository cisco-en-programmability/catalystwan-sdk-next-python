================================
multicloud.interconnect.services
================================


Operation: GET /dataservice/multicloud/interconnect/services
------------------------------------------------------------


API to retrieve the Interconnect Services Information from vManage.

.. code:: python

    def get_interconnect_services(
        interconnect_service_vendor_name: str,
        interconnect_type: str,
        interconnect_service_type: str,
    ) -> List[InterconnectService]: ...


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
        client.multicloud.interconnect.services.get_interconnect_services()


.. toctree::
    :maxdepth: 1

    models

