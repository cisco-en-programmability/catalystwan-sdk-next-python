=======================================
v1.feature_profile.nfvirtual.system.ntp
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp
-------------------------------------------------------------------------------


Create NTP Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateNfvirtualNtpParcelPostRequest
    ) -> CreateNfvirtualNtpParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.ntp.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
--------------------------------------------------------------------------------------


Get NTP Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, ntp_id: str
    ) -> GetSingleNfvirtualSystemNtpPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.ntp.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
--------------------------------------------------------------------------------------


Edit a  NTP Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        ntp_id: str,
        payload: EditNfvirtualNtpParcelPutRequest,
    ) -> EditNfvirtualNtpParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.ntp.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/ntp/{ntpId}
-----------------------------------------------------------------------------------------


Delete a NTP Profile Parcel for System feature profile

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
        client.v1.feature_profile.nfvirtual.system.ntp.delete()


.. toctree::
    :maxdepth: 1

    models

