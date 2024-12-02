=================================
util.logging.update_configuration
=================================


Operation: POST /dataservice/util/logging/updateConfiguration
-------------------------------------------------------------


Update logger configuration for rollover size and max file number

.. code:: python

    def update_logger_configuration(
        logger_name: LoggerNameParam,
        size_limit: Optional[int] = None,
        reset: Optional[bool] = False,
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
        client.util.logging.update_configuration.update_logger_configuration()


.. toctree::
    :maxdepth: 1

    models

