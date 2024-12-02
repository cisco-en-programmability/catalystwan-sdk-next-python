============================
ise.credentials.iseandpxgrid
============================


Operation: DELETE /dataservice/ise/credentials/iseandpxgrid
-----------------------------------------------------------


Delete PxGrid and Ise information on vManage. Also Deletes PxGrid Client on ISE

.. code:: python

    def delete_ise_and_px_grid_account() -> bool: ...


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
        client.ise.credentials.iseandpxgrid.delete_ise_and_px_grid_account()


