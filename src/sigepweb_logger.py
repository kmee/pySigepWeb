# -*- coding: utf-8 -*-


class SigepWebLogger(object):

    __instance = None

    def __init__(self):
        if self.__class__.__instance:
            raise Exception("""Tried to allocate a second
            instance of a singleton. Use get_instance() instead. """)

        self.__class__.__instance = self

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls()

        return cls.__instance