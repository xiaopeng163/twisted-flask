#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright 2012-2014
# See LICENSE for details.

""" Twisted server"""

from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

from api import app


class Echo(Protocol):

    def __init__(self):

        self.data_dict = {}

    def connectionMade(self):

        # Set transport socket options
        self.transport.setTcpNoDelay(True)
        self.data_dict[self.transport.getHost().host] = None

    def dataReceived(self, data):
        """
        As soon as any data is received, write it back.
        """
        self.data_dict[self.transport.getHost().host] = data
        print self.data_dict
        pass

    def send_to_peer(self):
        pass


def main():
    f = Factory()
    f.protocol = Echo
    reactor.listenTCP(8000, f)
    resource = WSGIResource(reactor, reactor.getThreadPool(), app)
    site = Site(resource)

    reactor.listenTCP(8080, site, interface="127.0.0.1")
    reactor.run()

if __name__ == '__main__':
    main()