==========================
multicloud.push_cgw_config
==========================


Operation: POST /dataservice/multicloud/pushCgwConfig
-----------------------------------------------------


Push configuration to devices of CGW

.. code:: python

    def push_cgw_cfg(
        payload: Optional[PushCgwConfig] = None,
    ) -> Taskid: ...


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
        client.multicloud.push_cgw_config.push_cgw_cfg()


.. toctree::
    :maxdepth: 1

    models

