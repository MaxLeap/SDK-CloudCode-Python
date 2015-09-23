# coding: utf-8

from StringIO import StringIO
from nose.tools import with_setup

import requests

import leapcloud
from leapcloud import File
from leapcloud import ACL

__author__ = 'czhou <czhou@ilegendsoft.com>'


def setup_func():
    leapcloud.init(
        '55d1480960b2430132e9b19e',
        'T2N5aGQxY25vLU9EMkJkdFNSQVY1dw',
    )


def test_basic():
    s = StringIO('blah blah blah')
    f = File('blah', s)
    assert f.name == 'blah'
    assert f._metadata['size'] == 14
    assert f._type == 'text/plain'


def test_create_with_url():
    f = File.create_with_url('xxx', 'http://www.lenna.org/full/len_std.jpg')
    assert f.url == 'http://www.lenna.org/full/len_std.jpg'


def test_create_without_data():
    f = File.create_without_data(123)
    assert f.id == 123


def test_acl():
    acl = ACL()
    f = File('blah', buffer('xxx'))
    f.set_acl(acl)
    assert f.get_acl() == acl


@with_setup(setup_func)
def test_save():
    f = File('blah', buffer('xxx'))
    f.save()
    assert f.url