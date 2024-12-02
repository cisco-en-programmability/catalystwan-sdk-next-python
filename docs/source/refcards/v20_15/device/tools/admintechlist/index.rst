==========================
device.tools.admintechlist
==========================


Operation: POST /dataservice/device/tools/admintechlist
-------------------------------------------------------


List admin tech logs

.. code:: python

    def list_admin_techs_on_device(
        payload: Optional[AdminTechListReq] = None,
    ) -> List[AdminTechListRes]: ...


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
        client.device.tools.admintechlist.list_admin_techs_on_device()


.. toctree::
    :maxdepth: 1

    models

