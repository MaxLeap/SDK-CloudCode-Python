# coding: utf-8

__author__ = 'czhou <czhou@ilegendsoft.com>'


class MaxLeapError(Exception):
    def __init__(self, code, error):
        self.code = code
        self.error = error

    def __str__(self):
        error = self.error if isinstance(self.error, str) else self.error.encode('utf-8', 'ignore')
        return '[{0}] {1}'.format(self.code, error)
