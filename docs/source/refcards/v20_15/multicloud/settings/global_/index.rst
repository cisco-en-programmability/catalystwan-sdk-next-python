===========================
multicloud.settings.global_
===========================


Operation: GET /dataservice/multicloud/settings/global
------------------------------------------------------


Get global settings

.. code:: python

    def get_global_settings(
        cloud_type: CloudTypeParam,
    ) -> GlobalSettings: ...


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
        client.multicloud.settings.global_.get_global_settings()


Operation: PUT /dataservice/multicloud/settings/global
------------------------------------------------------


Update global settings

.. code:: python

    def update_global_settings(
        payload: Optional[GlobalSettings] = None,
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
        client.multicloud.settings.global_.update_global_settings()


Operation: POST /dataservice/multicloud/settings/global
-------------------------------------------------------


Add global settings

.. code:: python

    def add_global_settings(
        payload: Optional[GlobalSettings] = None,
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
        client.multicloud.settings.global_.add_global_settings()


.. toctree::
    :maxdepth: 1

    models

