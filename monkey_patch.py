# dynamic replacement of attributes at runtime.


def square(value):
	return value ** 2


def cube(value):
	return value ** 3

def main(value):
	return square(value) + cube(value)


try:
	import mock
except ImportError
	from unittest import mock

import unittest
from function import square, main
