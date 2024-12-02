=============================================================================
multicloud.interconnect.accounts.cloud.connectivity.connections.partner_ports
=============================================================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/cloud/{cloud-type}/connectivity/connections/partner-ports
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


API to retrieve supported partner regions for an Interconnect provider.

.. code:: python

    def get_interconnect_partner_ports(
        interconnect_type: str,
        interconnect_account_id: str,
        cloud_type: str,
        connect_type: Optional[str] = None,
        vxc_permitted: Optional[str] = None,
        authorization_key: Optional[str] = None,
        refresh: Optional[str] = "false",
    ) -> InlineResponse2006: ...


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
        client.multicloud.interconnect.accounts.cloud.connectivity.connections.partner_ports.get_interconnect_partner_ports()


.. toctree::
    :maxdepth: 1

    models

