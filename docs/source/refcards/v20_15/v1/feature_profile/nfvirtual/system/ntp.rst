=======================================
v1.feature_profile.nfvirtual.system.ntp
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp
-------------------------------------------------------------------------------


Create NTP Profile Parcel for System feature profile

.. code:: python

    def create_nfvirtual_ntp_parcel(
        system_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.ntp.create_nfvirtual_ntp_parcel()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
--------------------------------------------------------------------------------------


Get NTP Profile Parcels for System feature profile

.. code:: python

    def get_nfvirtual_ntp_parcel(system_id: str, ntp_id: str) -> str: ...


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
        client.v1.feature_profile.nfvirtual.system.ntp.get_nfvirtual_ntp_parcel()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
--------------------------------------------------------------------------------------


Edit a  NTP Profile Parcel for System feature profile

.. code:: python

    def edit_nfvirtual_ntp_parcel(
        system_id: str, ntp_id: str, payload: Optional[str] = None
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
        client.v1.feature_profile.nfvirtual.system.ntp.edit_nfvirtual_ntp_parcel()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
-----------------------------------------------------------------------------------------


Delete a NTP Profile Parcel for System feature profile

.. code:: python

    def delete_nfvirtual_ntp_parcel(
        system_id: str, ntp_id: str
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
        client.v1.feature_profile.nfvirtual.system.ntp.delete_nfvirtual_ntp_parcel()


