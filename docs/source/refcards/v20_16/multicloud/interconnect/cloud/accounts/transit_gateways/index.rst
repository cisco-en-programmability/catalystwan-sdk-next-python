=======================================================
multicloud.interconnect.cloud.accounts.transit_gateways
=======================================================


Operation: GET /dataservice/multicloud/interconnect/cloud/{cloud-type}/accounts/{cloud-account-id}/transit-gateways
-------------------------------------------------------------------------------------------------------------------


API to retrieve AWS Transit Gateways.

.. code:: python

    def get(
        cloud_type: CloudTypeParam,
        cloud_account_id: str,
        transit_gateway_name: Optional[str] = None,
        region: Optional[str] = None,
        tag_name: Optional[str] = None,
        refresh: Optional[str] = "false",
    ) -> InlineResponse2008: ...


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
        client.multicloud.interconnect.cloud.accounts.transit_gateways.get()


.. toctree::
    :maxdepth: 1

    models

