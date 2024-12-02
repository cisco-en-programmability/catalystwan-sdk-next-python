===========
partner.map
===========


Operation: GET /dataservice/partner/{partnerType}/map/{nmsId}
-------------------------------------------------------------


List mapped devices for the partner

.. code:: python

    def get_partner_devices(
        partner_type: str, nms_id: str
    ) -> PartnerDevicesRes: ...


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
        client.partner.map.get_partner_devices()


Operation: POST /dataservice/partner/{partnerType}/map/{nmsId}
--------------------------------------------------------------


Map devices for the partner

.. code:: python

    def map_devices(
        partner_type: str, nms_id: str, payload: MapDevicesRequest
    ) -> StatusResponse: ...


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
        client.partner.map.map_devices()


Operation: DELETE /dataservice/partner/{partnerType}/map/{nmsId}
----------------------------------------------------------------


Unmap all devices for the partner

.. code:: python

    def unmap_devices(
        partner_type: str, nms_id: str
    ) -> StatusResponse: ...


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
        client.partner.map.unmap_devices()


.. toctree::
    :maxdepth: 1

    models

