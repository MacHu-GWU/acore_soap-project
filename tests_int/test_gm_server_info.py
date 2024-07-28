# -*- coding: utf-8 -*-

from acore_soap.gm.server_info import ServerInfoRequest, ServerInfoResponse


def test():
    soap_response = ServerInfoRequest().send()
    server_info_response = ServerInfoResponse.from_soap_response(soap_response)
    print(f"{server_info_response.connected_players = }")
    print(f"{server_info_response.characters_in_world = }")
    print(f"{server_info_response.server_uptime = }")


if __name__ == "__main__":
    from acore_soap.tests import run_cov_test

    run_cov_test(__file__, "acore_soap.gm.server_info", preview=False)
