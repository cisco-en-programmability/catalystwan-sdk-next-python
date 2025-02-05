=================================
multicloud.interconnect.locations
=================================


Operation: DELETE /dataservice/multicloud/interconnect/{interconnect-type}/locations
------------------------------------------------------------------------------------


API to delete the stored regions for an Interconnect provider type from vManage.

.. code:: python

    def delete_all_interconnect_location_info(
        interconnect_type: str,
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
        client.multicloud.interconnect.locations.delete_all_interconnect_location_info()


