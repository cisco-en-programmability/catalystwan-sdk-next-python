=================
ise.pxgrid.create
=================


Operation: POST /dataservice/ise/pxgrid/create
----------------------------------------------


Create pxGrid account

.. code:: python

    def account_create(
        payload: Optional[CreateBody] = None,
    ) -> CreateResponse: ...


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
        client.ise.pxgrid.create.account_create()


.. toctree::
    :maxdepth: 1

    models

