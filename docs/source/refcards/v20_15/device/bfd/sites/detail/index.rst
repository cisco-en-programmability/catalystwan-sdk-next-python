=======================
device.bfd.sites.detail
=======================


Operation: GET /dataservice/device/bfd/sites/detail
---------------------------------------------------


Get detailed BFD site details

.. code:: python

    def get(state: Optional[StateParam] = None) -> Any: ...


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
        client.device.bfd.sites.detail.get()


.. toctree::
    :maxdepth: 1

    models

