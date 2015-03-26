# -*- coding: utf-8 -*-


class TagBase(object):

    def xml(self):
        raise NotImplementedError("Must subclass me")

