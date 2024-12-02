==============================
device.tools.admintechs.upload
==============================


Operation: POST /dataservice/device/tools/admintechs/upload
-----------------------------------------------------------


upload admin tech to SR

.. code:: python

    def upload_admin_tech(
        payload: Optional[AdminTechsUploadReq] = None,
    ) -> None: ...


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
        client.device.tools.admintechs.upload.upload_admin_tech()


.. toctree::
    :maxdepth: 1

    models

