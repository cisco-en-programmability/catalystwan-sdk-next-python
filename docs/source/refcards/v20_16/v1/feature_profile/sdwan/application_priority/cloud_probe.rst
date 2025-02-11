=========================================================
v1.feature_profile.sdwan.application_priority.cloud_probe
=========================================================


Operation: GET /dataservice/v1/feature-profile/sdwan/application-priority/{applicationPriorityId}/cloud-probe/{cloudProbeId}
----------------------------------------------------------------------------------------------------------------------------


Get Cloud Probe Profile Parcel by parcelId for application-priority feature profile

.. code:: python

    def get_cloud_probe_profile_parcel_by_parcel_id_forapplication_priority(
        application_priority_id: str, cloud_probe_id: str
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
        client.v1.feature_profile.sdwan.application_priority.cloud_probe.get_cloud_probe_profile_parcel_by_parcel_id_forapplication_priority()


