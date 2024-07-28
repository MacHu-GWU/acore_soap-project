# -*- coding: utf-8 -*-

"""
This module provides a parser for the response message of GM commands.

See all sample GM commands response message at
https://github.com/MacHu-GWU/acore_soap_app-project/blob/main/tests/gm/test_parser.py

Reference:

- https://www.azerothcore.org/wiki/gm-commands
"""

import typing as T
import re
import dataclasses

from ..exc import SOAPResponseParseError
from ..agent.api import SOAPResponse


@dataclasses.dataclass
class GMCommandResponse:
    @classmethod
    def from_soap_response(self, res: SOAPResponse):
        raise NotImplementedError


T_GM_COMMAND_RESPONSE = T.TypeVar("T_GM_COMMAND_RESPONSE", bound=GMCommandResponse)


@dataclasses.dataclass
class ServerInfoResponse:
    """
    Parse the response message of ``.server info`` command, extract

    :param connected_players: how many players are logged in.
    :param characters_in_world: how many player
    :param server_uptime: how long the server has been running (in seconds)
    """

    connected_players: int
    characters_in_world: int
    server_uptime: int

    @staticmethod
    def extract_connected_players(message: str) -> int:
        """
        Extract the number of connected players from the response message.
        """
        res = re.findall(r"Connected players: (\d+)", message)
        if len(res) == 1:
            return int(res[0])
        else:  # pragma: no cover
            raise SOAPResponseParseError(message)

    @staticmethod
    def extract_characters_in_world(message: str) -> int:
        """
        Extract the number of characters in the world from the response message.
        """
        res = re.findall(r"Characters in world: (\d+)", message)
        if len(res) == 1:
            return int(res[0])
        else:  # pragma: no cover
            raise SOAPResponseParseError(message)

    @staticmethod
    def extract_server_uptime(message: str) -> int:
        """
        Extract the server uptime from the response message.
        """
        P_SECOND = re.compile("(\d+\s+second\(s\))")
        P_MINUTE = re.compile("(\d+\s+minute\(s\))")
        P_HOUR = re.compile("(\d+\s+hour\(s\))")
        P_DAY = re.compile("(\d+\s+day\(s\))")

        def extract(p: re.Pattern, message: str) -> int:
            res = re.findall(p, message)
            if len(res) == 1:
                return int(res[0].split()[0])
            elif len(res) == 0:
                return 0
            else:  # pragma: no cover
                raise ValueError()

        seconds = extract(P_SECOND, message)
        minutes = extract(P_MINUTE, message)
        hours = extract(P_HOUR, message)
        days = extract(P_DAY, message)
        total_seconds = seconds + minutes * 60 + hours * 3600 + days * 86400
        return total_seconds

    @classmethod
    def from_soap_response(self, res: SOAPResponse):
        connected_players = self.extract_connected_players(res.message)
        characters_in_world = self.extract_characters_in_world(res.message)
        server_uptime = self.extract_server_uptime(res.message)
        return ServerInfoResponse(
            connected_players=connected_players,
            characters_in_world=characters_in_world,
            server_uptime=server_uptime,
        )
