==================================
device.tools.admintechs.inprogress
==================================


Operation: GET /dataservice/device/tools/admintechs/inprogress
--------------------------------------------------------------


Get device admin-tech InProgressCount

.. code:: python

    def get() -> InProgressCount: ...


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
        client.device.tools.admintechs.inprogress.get()


.. toctree::
    :maxdepth: 1

    models

