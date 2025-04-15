===========================
multicloud.settings.global_
===========================


Operation: GET /dataservice/multicloud/settings/global
------------------------------------------------------


Get global settings

.. code:: python

    def get(cloud_type: CloudTypeParam) -> GlobalSettings: ...


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
        client.multicloud.settings.global_.get()


Operation: PUT /dataservice/multicloud/settings/global
------------------------------------------------------


Update global settings

.. code:: python

    def put(payload: GlobalSettings) -> None: ...


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
        client.multicloud.settings.global_.put()


Operation: POST /dataservice/multicloud/settings/global
-------------------------------------------------------


Add global settings

.. code:: python

    def post(payload: GlobalSettings) -> Taskid: ...


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
        client.multicloud.settings.global_.post()


.. toctree::
    :maxdepth: 1

    models

