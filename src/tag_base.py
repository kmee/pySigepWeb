# -*- coding: utf-8 -*-


class TagBase(object):

    def get_xml(self):
        raise NotImplementedError("Must subclass me")
