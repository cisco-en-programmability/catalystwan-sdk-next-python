======================
ise.credentials.pxgrid
======================


Operation: GET /dataservice/ise/credentials/pxgrid
--------------------------------------------------


Get PxGrid account

.. code:: python

    def get_px_grid_account() -> PxGridInfo: ...


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
        client.ise.credentials.pxgrid.get_px_grid_account()


Operation: DELETE /dataservice/ise/credentials/pxgrid
-----------------------------------------------------


Delete PxGrid account information

.. code:: python

    def delete_px_grid() -> bool: ...


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
        client.ise.credentials.pxgrid.delete_px_grid()


.. toctree::
    :maxdepth: 1

    cert
    models

