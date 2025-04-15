====================================================
v1.feature_profile.mobility.global_.network_protocol
====================================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol
-------------------------------------------------------------------------------------------


Create an NetworkProtocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateNetworkProtocolProfileParcelForMobilityPostRequest,
    ) -> str: ...


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
        client.v1.feature_profile.mobility.global_.network_protocol.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
--------------------------------------------------------------------------------------------------------------


Edit an Network Protocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def put(
        profile_id: str,
        network_protocol_id: str,
        payload: EditNetworkProtocolProfileParcelForMobilityPutRequest,
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
        client.v1.feature_profile.mobility.global_.network_protocol.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
-----------------------------------------------------------------------------------------------------------------


Delete a Network Protocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete(profile_id: str, network_protocol_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.network_protocol.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol
------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str,
    ) -> GetListMobilityGlobalNetworkprotocolPayload: ...


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
        client.v1.feature_profile.mobility.global_.network_protocol.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
--------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, network_protocol_id: str
    ) -> GetSingleMobilityGlobalNetworkprotocolPayload: ...


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
        client.v1.feature_profile.mobility.global_.network_protocol.get()


.. toctree::
    :maxdepth: 1

    models

