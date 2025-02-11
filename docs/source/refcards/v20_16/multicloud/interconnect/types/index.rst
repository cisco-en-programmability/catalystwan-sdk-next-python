=============================
multicloud.interconnect.types
=============================


Operation: GET /dataservice/multicloud/interconnect/types
---------------------------------------------------------


API to retrieve list of supported Interconnect provider Types.

.. code:: python

    def get_interconnect_types() -> InlineResponse200: ...


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
        client.multicloud.interconnect.types.get_interconnect_types()


.. toctree::
    :maxdepth: 1

    models

