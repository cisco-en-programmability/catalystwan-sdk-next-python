===========
partner.map
===========


Operation: GET /dataservice/partner/{partnerType}/map/{nmsId}
-------------------------------------------------------------


List mapped devices for the partner

.. code:: python

    def get(partner_type: str, nms_id: str) -> PartnerDevicesRes: ...


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
        client.partner.map.get()


Operation: POST /dataservice/partner/{partnerType}/map/{nmsId}
--------------------------------------------------------------


Map devices for the partner

.. code:: python

    def post(
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
        client.partner.map.post()


Operation: DELETE /dataservice/partner/{partnerType}/map/{nmsId}
----------------------------------------------------------------


Unmap all devices for the partner

.. code:: python

    def delete(partner_type: str, nms_id: str) -> StatusResponse: ...


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
        client.partner.map.delete()


.. toctree::
    :maxdepth: 1

    models

