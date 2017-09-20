#!/usr/bin/python
# -*- coding:utf-8 -*-
import random

# autoscaling group
class ASG:
    def __init__(self, ID, type, servers):
        # type :  0: DPI0  1 :DPI1  2: DPI2 3: DPI3
        self.ID = ID
        self.type = type
        self.servers = servers

    def __str__(self):
        info = "ASG-" + str(self.ID) + " : "
        info += "type : " + str(self.type) + ","
        info += "server list: "
        if self.servers is not None:
            for server in self.servers:
                info += str(server.ID) + " "
        return info

    def add_server(self, server):
        self.servers.append(server)

    def remove_server(self, server):
        self.servers.remove(server)

    def get_server_by_status(self, status):
        servers = []
        for server in self.servers:
            if server.status == status:
                servers.append(server)
        return servers


def shuffle_asg(num):
    # generate <num> of random asgs
    asgs = []
    for i in range(num):
        type = random.randint(0, 3)
        asgs.append(ASG(i, type, None))
    return asgs