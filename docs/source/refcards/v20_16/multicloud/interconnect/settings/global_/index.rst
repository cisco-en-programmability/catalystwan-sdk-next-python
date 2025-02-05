========================================
multicloud.interconnect.settings.global_
========================================


Operation: GET /dataservice/multicloud/interconnect/settings/global
-------------------------------------------------------------------


API to retrieve global settings for an Interconnect provider type.

.. code:: python

    def get_interconnect_global_settings(
        interconnect_type: InterconnectTypeParam,
    ) -> InterconnectGlobalSettings: ...


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
        client.multicloud.interconnect.settings.global_.get_interconnect_global_settings()


Operation: PUT /dataservice/multicloud/interconnect/settings/global
-------------------------------------------------------------------


API to update global settings for an Interconnect provider.

.. code:: python

    def update_interconnect_global_settings(
        payload: Optional[InterconnectGlobalSettings] = None,
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
        client.multicloud.interconnect.settings.global_.update_interconnect_global_settings()


Operation: POST /dataservice/multicloud/interconnect/settings/global
--------------------------------------------------------------------


API to add global settings for an Interconnect provider.

.. code:: python

    def add_interconnect_global_settings(
        payload: Optional[InterconnectGlobalSettings] = None,
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
        client.multicloud.interconnect.settings.global_.add_interconnect_global_settings()


.. toctree::
    :maxdepth: 1

    models

