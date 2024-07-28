# -*- coding: utf-8 -*-

from acore_soap.request import SOAPRequest


def test():
    soap_response = SOAPRequest(command=".server info").send()
    print(f"{soap_response.body = }")
    print(f"{soap_response.message = }")
    print(f"{soap_response.succeeded = }")


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.request", preview=False)
