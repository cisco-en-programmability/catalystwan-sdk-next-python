===============
template.cortex
===============


Operation: GET /dataservice/template/cortex
-------------------------------------------


Get Cortex List

.. code:: python

    def get_cortex_status() -> List[Any]: ...


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
        client.template.cortex.get_cortex_status()


.. toctree::
    :maxdepth: 1

    cloud/index
    map
    sync
    wanrg

