=================================================
multicloud.interconnect.connectivity.device_links
=================================================


Operation: GET /dataservice/multicloud/interconnect/connectivity/device-links
-----------------------------------------------------------------------------


API to retrieve Interconnect provider Device-Link.

.. code:: python

    def get_interconnect_device_links(
        device_link_name: Optional[str] = None,
        interconnect_type: Optional[InterconnectTypeParam] = None,
        refresh: Optional[str] = "false",
    ) -> InterconnectDeviceLink: ...


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
        client.multicloud.interconnect.connectivity.device_links.get_interconnect_device_links()


Operation: POST /dataservice/multicloud/interconnect/connectivity/device-links
------------------------------------------------------------------------------


API to create a Device-Link in vManage.

.. code:: python

    def add_interconnect_device_link(
        payload: Optional[InterconnectDeviceLink] = None,
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.device_links.add_interconnect_device_link()


Operation: GET /dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}
------------------------------------------------------------------------------------------------


API to retrieve Interconnect provider Device-Link.

.. code:: python

    def get_interconnect_device_link(
        device_link_name: str,
    ) -> InterconnectDeviceLink: ...


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
        client.multicloud.interconnect.connectivity.device_links.get_interconnect_device_link()


Operation: PUT /dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}
------------------------------------------------------------------------------------------------


API to update a Device-Link in vManage.

.. code:: python

    def update_interconnect_device_link(
        device_link_name: str,
        payload: Optional[InterconnectDeviceLink] = None,
    ) -> ProcessResponse: ...


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
        client.multicloud.interconnect.connectivity.device_links.update_interconnect_device_link()


Operation: DELETE /dataservice/multicloud/interconnect/connectivity/device-links/{device-link-name}
---------------------------------------------------------------------------------------------------


API to Delete Interconnect provider Device-Link.

.. code:: python

    def delete_interconnect_device_link(
        device_link_name: str,
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
        client.multicloud.interconnect.connectivity.device_links.delete_interconnect_device_link()


.. toctree::
    :maxdepth: 1

    metro_speed/index
    port_speeds/index
    models

