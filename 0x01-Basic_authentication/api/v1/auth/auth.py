#!/usr/bin/env python3
""" Auth module for API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth """
        return False

        def authorization_header(self, request=None) -> str:
            """ Authorization header """
            return None

        def current_user(self, request=None) -> TypeVar('User'):
            """ Current user """
            return None
