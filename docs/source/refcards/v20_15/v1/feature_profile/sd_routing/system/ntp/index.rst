========================================
v1.feature_profile.sd_routing.system.ntp
========================================


Operation: POST /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp
--------------------------------------------------------------------------------


Create a SD-Routing NTP Feature for System Feature Profile

.. code:: python

    def post(
        system_id: str, payload: CreateSdroutingNtpFeaturePostRequest
    ) -> CreateSdroutingNtpFeaturePostResponse: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.post()


Operation: PUT /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
---------------------------------------------------------------------------------------


Edit a SD-Routing NTP Feature for System Feature Profile

.. code:: python

    def put(
        system_id: str,
        ntp_id: str,
        payload: EditSdroutingNtpFeaturePutRequest,
    ) -> EditSdroutingNtpFeaturePutResponse: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.put()


Operation: DELETE /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
------------------------------------------------------------------------------------------


Delete a SD-Routing NTP Feature for System Feature Profile

.. code:: python

    def delete(system_id: str, ntp_id: str) -> None: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.delete()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp
-------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str,
    ) -> GetListSdRoutingSystemNtpSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.get()


Operation: GET /dataservice/v1/feature-profile/sd-routing/system/{systemId}/ntp/{ntpId}
---------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, ntp_id: str
    ) -> GetSingleSdRoutingSystemNtpSdRoutingPayload: ...


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
        client.v1.feature_profile.sd_routing.system.ntp.get()


.. toctree::
    :maxdepth: 1

    models

