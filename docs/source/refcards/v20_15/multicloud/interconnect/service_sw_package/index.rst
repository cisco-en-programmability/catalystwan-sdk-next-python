==========================================
multicloud.interconnect.service_sw_package
==========================================


Operation: GET /dataservice/multicloud/interconnect/service-sw-package
----------------------------------------------------------------------


API to retrieve the Interconnect Services Sw Package Types Information from vManage.

.. code:: python

    def get(
        interconnect_provider_name: str,
        interconnect_account_id: str,
        interconnect_service_type: str,
        interconnect_service_vendor_name: str,
        region: Optional[str] = None,
    ) -> InlineResponse20015: ...


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
        client.multicloud.interconnect.service_sw_package.get()


.. toctree::
    :maxdepth: 1

    models

