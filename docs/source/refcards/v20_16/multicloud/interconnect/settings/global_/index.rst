========================================
multicloud.interconnect.settings.global_
========================================


Operation: GET /dataservice/multicloud/interconnect/settings/global
-------------------------------------------------------------------


API to retrieve global settings for an Interconnect provider type.

.. code:: python

    def get(
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
        client.multicloud.interconnect.settings.global_.get()


Operation: PUT /dataservice/multicloud/interconnect/settings/global
-------------------------------------------------------------------


API to update global settings for an Interconnect provider.

.. code:: python

    def put(payload: InterconnectGlobalSettings) -> None: ...


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
        client.multicloud.interconnect.settings.global_.put()


Operation: POST /dataservice/multicloud/interconnect/settings/global
--------------------------------------------------------------------


API to add global settings for an Interconnect provider.

.. code:: python

    def post(payload: InterconnectGlobalSettings) -> None: ...


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
        client.multicloud.interconnect.settings.global_.post()


.. toctree::
    :maxdepth: 1

    models

