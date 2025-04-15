=======
partner
=======


Operation: POST /dataservice/partner/{partnerType}
--------------------------------------------------


Register NMS partner

.. code:: python

    def post(
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
        client.partner.post()


Operation: PUT /dataservice/partner/{partnerType}/{nmsId}
---------------------------------------------------------


Update NMS partner details

.. code:: python

    def put(
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
        client.partner.put()


Operation: DELETE /dataservice/partner/{partnerType}/{nmsId}
------------------------------------------------------------


Delete NMS partner

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
        client.partner.delete()


Operation: GET /dataservice/partner
-----------------------------------


.. code:: python

    @overload
    def get() -> List[PartnerRes]: ...


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
        client.partner.get()


Operation: GET /dataservice/partner/{partnerType}
-------------------------------------------------


.. code:: python

    @overload
    def get(partner_type: str) -> List[PartnerRes]: ...


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
        client.partner.get()


Operation: GET /dataservice/partner/{partnerType}/{nmsId}
---------------------------------------------------------


.. code:: python

    @overload
    def get(partner_type: str, nms_id: str) -> PartnerRes: ...


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
        client.partner.get()


.. toctree::
    :maxdepth: 1

    aci/index
    dnac/index
    vpn/index
    wcm/index
    map/index
    unmap/index
    models

