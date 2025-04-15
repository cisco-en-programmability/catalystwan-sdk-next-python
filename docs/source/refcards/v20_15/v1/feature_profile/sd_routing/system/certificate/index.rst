================================================
v1.feature_profile.sd_routing.system.certificate
================================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate
----------------------------------------------------------------------------------------


Create a SD-Routing Certificate Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateSdroutingCertificateFeaturePostRequest,
    ) -> CreateSdroutingCertificateFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
-------------------------------------------------------------------------------------------------------


Edit a SD-Routing Certificate Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        certificate_id: str,
        payload: EditSdroutingCertificateFeaturePutRequest,
    ) -> EditSdroutingCertificateFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
----------------------------------------------------------------------------------------------------------


Delete a SD-Routing Certificate Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, certificate_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate
---------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemCertificatePayload: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/certificate/{certificateId}
-------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, certificate_id: str
    ) -> GetSingleSdRoutingSystemCertificatePayload: ...


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
        client.v1.feature_profile.sd_routing.system.certificate.get()


.. toctree::
    :maxdepth: 1

    models

