========================
event.component.keyvalue
========================


Operation: GET /dataservice/event/component/keyvalue
----------------------------------------------------


Get event component types.

.. code:: python

    def get_components_as_key_value() -> SimpleKeyValueMapping: ...


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
        client.event.component.keyvalue.get_components_as_key_value()


.. toctree::
    :maxdepth: 1

    models

