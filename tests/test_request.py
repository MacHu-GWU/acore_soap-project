# -*- coding: utf-8 -*-

import pytest
from acore_soap.request import (
    SOAPRequest,
    SOAPResponse,
    ensure_response_succeeded,
    SOAPCommandFailedError,
)


def test():
    soap_request = SOAPRequest(command=".server info")
    soap_response = SOAPResponse(
        body="this is body", message="this is message", succeeded=True
    )
    ensure_response_succeeded(
        request=soap_request,
        response=soap_response,
        raises=True,
    )

    soap_response = SOAPResponse(
        body="this is body", message="this is message", succeeded=False
    )
    with pytest.raises(SOAPCommandFailedError):
        ensure_response_succeeded(
            request=soap_request,
            response=soap_response,
            raises=True,
        )


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.request", preview=False)
