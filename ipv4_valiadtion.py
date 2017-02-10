# -*- coding: utf-8 -*-

import socket
import ipaddress
import re

ip_str = '192.168.1.100'
ip_str2 = 'test.12.3'

def ip_validation_re(ip_str):
	"""正则 ip v4的具体地址规则应该更详细符合RFC IPv4 规范"""
	pattern =r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
	if re.match(pattern,ip_str):
		return True
	return False

def ip_validation_address(ip_str):
	"""Python 内置的ip地址功能"""
	try:
		if type(ipaddress.ip_address(ip_str)) == ipaddress.IPv4Address:
			return True
	except ValueError:
		return False

def ip_validation_aton(ip_str):
	"""Python 内置的ip地址功能"""
	try:
		socket.inet_aton(ip_str)
		return True
	except socket.error:
		return False

print(ip_validation_re(ip_str))
print(ip_validation_address(ip_str))
print(ip_validation_aton(ip_str))
print(ip_validation_re(ip_str2))
print(ip_validation_address(ip_str2))
print(ip_validation_aton(ip_str2))



