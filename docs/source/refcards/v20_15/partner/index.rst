=======
partner
=======


Operation: GET /dataservice/partner
-----------------------------------


Get all NMS partners

.. code:: python

    def get_partners() -> List[PartnerRes]: ...


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
        client.partner.get_partners()


Operation: GET /dataservice/partner/{partnerType}
-------------------------------------------------


Get NMS partners by partner type

.. code:: python

    def get_partners_by_partner_type(
        partner_type: str,
    ) -> List[PartnerRes]: ...


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
        client.partner.get_partners_by_partner_type()


Operation: POST /dataservice/partner/{partnerType}
--------------------------------------------------


Register NMS partner

.. code:: python

    def register_partner(
        partner_type: str, payload: RegisterPartnerRequest
    ) -> RegisterPartnerRes: ...


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
        client.partner.register_partner()


Operation: GET /dataservice/partner/{partnerType}/{nmsId}
---------------------------------------------------------


Get NMS partners by partner type and Id

.. code:: python

    def get_partner(partner_type: str, nms_id: str) -> PartnerRes: ...


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
        client.partner.get_partner()


Operation: PUT /dataservice/partner/{partnerType}/{nmsId}
---------------------------------------------------------


Update NMS partner details

.. code:: python

    def update_partner(
        partner_type: str, nms_id: str, payload: UpdatePartnerRequest
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
        client.partner.update_partner()


Operation: DELETE /dataservice/partner/{partnerType}/{nmsId}
------------------------------------------------------------


Delete NMS partner

.. code:: python

    def delete_partner(
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
        client.partner.delete_partner()


.. toctree::
    :maxdepth: 1

    aci/index
    dnac/index
    vpn/index
    wcm/index
    map/index
    unmap/index
    models

