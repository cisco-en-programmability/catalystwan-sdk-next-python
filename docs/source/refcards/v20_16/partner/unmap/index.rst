=============
partner.unmap
=============


Operation: POST /dataservice/partner/{partnerType}/unmap/{nmsId}
----------------------------------------------------------------


Unmap a set of devices for the partner

.. code:: python

    def delete_device_mapping(
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
        client.partner.unmap.delete_device_mapping()


.. toctree::
    :maxdepth: 1

    models

