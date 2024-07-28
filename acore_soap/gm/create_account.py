# -*- coding: utf-8 -*-

"""
todo: docstring
"""

import re
import dataclasses

from ..request import SOAPResponse
from ..exc import SOAPResponseParseError

from .base import GMCommandRequest, GMCommandResponse


@dataclasses.dataclass
class CreateAccountResponse(GMCommandResponse):
    """
    Parse the response message of ``.account create ...`` command.
    """

    @classmethod
    def from_soap_response(cls, res: SOAPResponse):
        raise NotImplementedError


@dataclasses.dataclass
class CreateAccountRequest(GMCommandRequest):
    """
    todo: docstring
    """

    account: str = dataclasses.field()
    password: str = dataclasses.field()

    def to_command(self) -> str:
        return f".account create {self.account} {self.password}"
