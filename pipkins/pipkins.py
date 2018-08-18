#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Authors:
#     Dario Maiocchi <dmaiocchi@suse.com>

import jenkins

server = jenkins.Jenkins(jenkins_server, username=user, password=pwd)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
