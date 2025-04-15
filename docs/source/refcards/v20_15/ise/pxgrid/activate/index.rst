===================
ise.pxgrid.activate
===================


Operation: POST /dataservice/ise/pxgrid/activate
------------------------------------------------


Activate pxGrid account

.. code:: python

    def post(payload: ActivateBody) -> ActivateResponse: ...


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
        client.ise.pxgrid.activate.post()


.. toctree::
    :maxdepth: 1

    models

