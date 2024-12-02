=============================
device.tools.admintech.delete
=============================


Operation: DELETE /dataservice/device/tools/admintech/delete
------------------------------------------------------------


delete admin tech logs

.. code:: python

    def delete_admin_tech_on_device(
        payload: Optional[AdminTechReq] = None,
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
        client.device.tools.admintech.delete.delete_admin_tech_on_device()


.. toctree::
    :maxdepth: 1

    models

