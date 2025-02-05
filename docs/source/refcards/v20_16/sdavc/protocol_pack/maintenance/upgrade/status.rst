==============================================
sdavc.protocol_pack.maintenance.upgrade.status
==============================================


Operation: GET /dataservice/sdavc/protocol-pack/maintenance/upgrade/status
--------------------------------------------------------------------------


Get active deploy job status

.. code:: python

    def get_deploy_job_status() -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.status.get_deploy_job_status()


Operation: GET /dataservice/sdavc/protocol-pack/maintenance/upgrade/status/{uuid}
---------------------------------------------------------------------------------


Get upgrade status for given Task UUID

.. code:: python

    def get_deploy_job_status_1(uuid: str) -> Any: ...


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
        client.sdavc.protocol_pack.maintenance.upgrade.status.get_deploy_job_status_1()


