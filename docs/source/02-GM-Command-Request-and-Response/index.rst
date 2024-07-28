GM Command Request and Response
==============================================================================
The :mod:`acore_soap.gm` module provides a set of more advanced class to send the GM command and parse the response message.

Each module in `acore_soap/gm/ <https://github.com/MacHu-GWU/acore_soap-project/tree/main/acore_soap/gm>`_ folder (Not include ``api.py`` and ``base.py``) implements one `Azerothcore GM command <https://www.azerothcore.org/wiki/gm-commands>`_.

Here are two examples:

.. dropdown:: server_info.py

    .. literalinclude:: ../../../acore_soap/gm/server_info.py
       :language: python
       :linenos:

.. dropdown:: create_account.py

    .. literalinclude:: ../../../acore_soap/gm/create_account.py
       :language: python
       :linenos:
