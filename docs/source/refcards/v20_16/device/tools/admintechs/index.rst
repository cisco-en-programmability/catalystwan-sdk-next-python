=======================
device.tools.admintechs
=======================


Operation: GET /dataservice/device/tools/admintechs
---------------------------------------------------


Get device admin-tech information

.. code:: python

    def get() -> List[AdminTechsRes]: ...


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
        client.device.tools.admintechs.get()


.. toctree::
    :maxdepth: 1

    inprogress/index
    upload/index
    models

