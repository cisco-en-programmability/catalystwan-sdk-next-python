============
tenantstatus
============


Operation: GET /dataservice/tenantstatus
----------------------------------------


List all tenant status<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider view.

.. code:: python

    def get() -> List[Any]: ...


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
        client.tenantstatus.get()


.. toctree::
    :maxdepth: 1

    force

