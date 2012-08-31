#!/usr/bin/env python

import sys, os, argparse
   
parser = argparse.ArgumentParser(description='How to get --version to work?')

parser.add_argument('--version', action='store_true', help='print version information')
parser.add_argument('-H', '--hostname', dest='hostname', required=True, help='Host name, IP Address')
parser.add_argument('-d', '--database', dest='database', required=True, help='Check database with indicated name')
parser.add_argument('-u', '--username', dest='username', required=True, help='connect using the indicated username')
parser.add_argument('-p', '--password', dest='password', required=True, help='use the indicated password to authenticate the connection')

args = parser.parse_args()

if args.version == True:
    print 'Version information here'