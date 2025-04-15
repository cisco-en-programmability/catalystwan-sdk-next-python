==========================
device.tools.admintechlist
==========================


Operation: POST /dataservice/device/tools/admintechlist
-------------------------------------------------------


List admin tech logs

.. code:: python

    def post(payload: AdminTechListReq) -> List[AdminTechListRes]: ...


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
        client.device.tools.admintechlist.post()


.. toctree::
    :maxdepth: 1

    models

