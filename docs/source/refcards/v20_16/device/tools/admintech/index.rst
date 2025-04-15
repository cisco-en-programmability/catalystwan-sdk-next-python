======================
device.tools.admintech
======================


Operation: POST /dataservice/device/tools/admintech
---------------------------------------------------


Generate admin tech logs

.. code:: python

    def post(payload: AdminTechCreateReq) -> None: ...


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
        client.device.tools.admintech.post()


Operation: DELETE /dataservice/device/tools/admintech/{requestID}
-----------------------------------------------------------------


Delete admin tech logs

.. code:: python

    def delete_admin_tech_file(request_id: str) -> None: ...


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
        client.device.tools.admintech.delete_admin_tech_file()


.. toctree::
    :maxdepth: 1

    copy/index
    delete/index
    download
    supportedfeatures/index
    models

