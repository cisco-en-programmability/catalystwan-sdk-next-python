====================================================
v1.feature_profile.mobility.global_.network_protocol
====================================================


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol
------------------------------------------------------------------------------------------


Get an Mobility NetworkProtocol Profile Parcel list for Mobility Global Feature Profile

.. code:: python

    def get_network_protocol_profile_parcel_list_for_mobility(
        profile_id: str,
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
        client.v1.feature_profile.mobility.global_.network_protocol.get_network_protocol_profile_parcel_list_for_mobility()


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol
-------------------------------------------------------------------------------------------


Create an NetworkProtocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def create_network_protocol_profile_parcel_for_mobility(
        profile_id: str,
        payload: Optional[
            CreateNetworkProtocolProfileParcelForMobilityPostRequest
        ] = None,
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
        client.v1.feature_profile.mobility.global_.network_protocol.create_network_protocol_profile_parcel_for_mobility()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
--------------------------------------------------------------------------------------------------------------


Get an Mobility NetworkProtocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def get_network_protocol_profile_parcel_for_mobility(
        profile_id: str, network_protocol_id: str
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
        client.v1.feature_profile.mobility.global_.network_protocol.get_network_protocol_profile_parcel_for_mobility()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
--------------------------------------------------------------------------------------------------------------


Edit an Network Protocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def edit_network_protocol_profile_parcel_for_mobility(
        profile_id: str,
        network_protocol_id: str,
        payload: Optional[
            CreateNetworkProtocolProfileParcelForMobilityPostRequest
        ] = None,
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
        client.v1.feature_profile.mobility.global_.network_protocol.edit_network_protocol_profile_parcel_for_mobility()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/networkProtocol/{networkProtocolId}
-----------------------------------------------------------------------------------------------------------------


Delete a Network Protocol Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def delete_network_protocol_profile_parcel_for_mobility(
        profile_id: str, network_protocol_id: str
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
        client.v1.feature_profile.mobility.global_.network_protocol.delete_network_protocol_profile_parcel_for_mobility()


.. toctree::
    :maxdepth: 1

    models

