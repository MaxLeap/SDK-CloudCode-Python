# coding: utf-8

import leapcloud


__author__ = 'czhou <czhou@ilegendsoft.com>'


def test_init():
    acl = leapcloud.ACL()
    role = leapcloud.Role('xxx', acl)
    assert role
    assert role.get_name() == 'xxx'
    assert role.get_acl() == acl
