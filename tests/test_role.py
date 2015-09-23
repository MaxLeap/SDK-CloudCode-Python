# coding: utf-8

import ML


__author__ = 'czhou <czhou@ilegendsoft.com>'


def test_init():
    acl = ML.ACL()
    role = ML.Role('xxx', acl)
    assert role
    assert role.get_name() == 'xxx'
    assert role.get_acl() == acl
