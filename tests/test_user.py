# coding: utf-8

from nose.tools import with_setup

import ML
from ML import User
from ML import Query
from ML import File

__author__ = 'czhou <czhou@ilegendsoft.com>'


def setup_func():
    ML.init(
        '55d1480960b2430132e9b19e',
        master_key='YURucS1ZcVUtS0w4Qmh4MW5IVWdFdw',
    )
    users = Query(User).find()
    for u in users:
        u.destroy()

    user1 = User()
    user1.set('username', 'username1')
    user1.set('password', 'password1')
    user1.sign_up()

    user2 = User()
    user2.set('username', 'username2')
    user2.set('password', 'password2')
    user2.sign_up()


def destroy_func():
    pass

@with_setup(setup_func, destroy_func)
def test_sign_up():
    user = User()
    user.set('username', 'neworgadmin')
    user.set('password', 'neworgadmin')
    user.sign_up()
    assert user._session_token


@with_setup(setup_func, destroy_func)
def test_login():
    user = User()
    user.set('username', 'username1')
    user.set('password', 'password1')
    user.login()

    user = User()
    user.login('username2', 'password2')

@with_setup(setup_func, destroy_func)
def test_file_field():
    user = User()
    user.login('username1', 'password1')
    user.set('xxxxx', File('xxx.txt', buffer('qqqqq')))
    user.save()

    q = Query(User)
    saved_user = q.get(user.id)
    assert isinstance(saved_user.get('xxxxx'), File)
