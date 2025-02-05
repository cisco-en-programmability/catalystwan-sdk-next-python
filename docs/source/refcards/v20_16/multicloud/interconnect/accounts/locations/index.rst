==========================================
multicloud.interconnect.accounts.locations
==========================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations
--------------------------------------------------------------------------------------------------------------------


API to retrieve list of available regions for an Interconnect provider and account.

.. code:: python

    def get_interconnect_location_info(
        interconnect_type: str,
        interconnect_account_id: str,
        region: Optional[str] = None,
    ) -> InterconnectLocations: ...


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
        client.multicloud.interconnect.accounts.locations.get_interconnect_location_info()


Operation: PUT /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations
--------------------------------------------------------------------------------------------------------------------


API to retrieve and update the available regions for an Interconnect provider and account.

.. code:: python

    def update_interconnect_location_info(
        interconnect_type: str, interconnect_account_id: str
    ) -> InterconnectLocations: ...


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
        client.multicloud.interconnect.accounts.locations.update_interconnect_location_info()


Operation: DELETE /dataservice/multicloud/interconnect/{interconnect-type}/accounts/{interconnect-account-id}/locations
-----------------------------------------------------------------------------------------------------------------------


API to delete the stored regions for an Interconnect provider and account from vManage.

.. code:: python

    def delete_interconnect_location_info(
        interconnect_type: str, interconnect_account_id: str
    ) -> None: ...


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
        client.multicloud.interconnect.accounts.locations.delete_interconnect_location_info()


.. toctree::
    :maxdepth: 1

    models

