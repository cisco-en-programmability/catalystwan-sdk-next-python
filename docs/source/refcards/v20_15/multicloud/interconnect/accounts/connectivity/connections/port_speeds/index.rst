=====================================================================
multicloud.interconnect.accounts.connectivity.connections.port_speeds
=====================================================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/connectivity/connections/{connection-type}/port-speeds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------


API to retrieve supported port speeds for an Interconnect connectivity.

.. code:: python

    def get(
        interconnect_type: str,
        interconnect_account_id: str,
        connection_type: str,
        cloud_type: Optional[str] = None,
        cloud_account_id: Optional[str] = None,
        connect_type: Optional[str] = None,
        connect_subtype: Optional[str] = None,
        connectivity_gateway_name: Optional[str] = None,
        partner_port: Optional[str] = None,
    ) -> InlineResponse2007: ...


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
        client.multicloud.interconnect.accounts.connectivity.connections.port_speeds.get()


.. toctree::
    :maxdepth: 1

    models

