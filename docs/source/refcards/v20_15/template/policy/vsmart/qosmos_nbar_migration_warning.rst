====================================================
template.policy.vsmart.qosmos_nbar_migration_warning
====================================================


Operation: GET /dataservice/template/policy/vsmart/qosmos_nbar_migration_warning
--------------------------------------------------------------------------------


Qosmos Nbar migration

.. code:: python

    def qosmos_nbar_migration_warning() -> Any: ...


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
        client.template.policy.vsmart.qosmos_nbar_migration_warning.qosmos_nbar_migration_warning()


