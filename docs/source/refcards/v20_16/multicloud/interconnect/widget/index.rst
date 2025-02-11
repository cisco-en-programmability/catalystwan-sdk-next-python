==============================
multicloud.interconnect.widget
==============================


Operation: GET /dataservice/multicloud/interconnect/widget
----------------------------------------------------------


API to retrieve all Interconnect widgets.

.. code:: python

    def get_all_interconnect_widgets() -> List[InterconnectWidget]: ...


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
        client.multicloud.interconnect.widget.get_all_interconnect_widgets()


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/widget
------------------------------------------------------------------------------


API to retrieve an Interconnect widget for an Interconnect type.

.. code:: python

    def get_interconnect_widget(
        interconnect_type: str,
    ) -> InterconnectWidget: ...


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
        client.multicloud.interconnect.widget.get_interconnect_widget()


.. toctree::
    :maxdepth: 1

    models

