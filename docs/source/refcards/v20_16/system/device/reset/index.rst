===================
system.device.reset
===================


Operation: PUT /dataservice/system/device/reset/{uuid}
------------------------------------------------------


Reset vEdge device

.. code:: python

    def reset_vedge_cloud(uuid: str) -> ResetVedgeCloud: ...


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
        client.system.device.reset.reset_vedge_cloud()


.. toctree::
    :maxdepth: 1

    models

