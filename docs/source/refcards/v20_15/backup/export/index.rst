=============
backup.export
=============


Operation: POST /dataservice/backup/export
------------------------------------------


Trigger a backup of configuration database and statstics database and store it in vManage

.. code:: python

    def post(payload: LocalBackupInfo) -> InlineResponse200: ...


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
        client.backup.export.post()


.. toctree::
    :maxdepth: 1

    models

