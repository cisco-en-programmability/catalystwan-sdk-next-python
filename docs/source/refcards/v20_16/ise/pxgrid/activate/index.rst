===================
ise.pxgrid.activate
===================


Operation: POST /dataservice/ise/pxgrid/activate
------------------------------------------------


Activate pxGrid account

.. code:: python

    def account_activate(
        payload: Optional[ActivateBody] = None,
    ) -> ActivateResponse: ...


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
        client.ise.pxgrid.activate.account_activate()


.. toctree::
    :maxdepth: 1

    models

