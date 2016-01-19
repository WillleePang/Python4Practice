# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

# 一开始的代码照常是模块导入部分。
# 要注意 twisted.internet 中 protocol 和 reactor 包和端口号常量。
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

# 我们从 Protocol 类中派生出 TSServProtocol 类做为时间戳服务器。
class TSServProtocol(protocol.Protocol):
    # 这个函数在有客户连接的时候被调用
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt

    # 这个函数在客户通过网络发送数据过来时被调用
    # reactor 把数据当成参数传到这个函数中，这样我们就不用自己去解析数据了。
    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

# 在服务器的最后一部分，我们创建一个 protocol 工厂。
# 它被称为“工厂”是因为，每次我们有连接进来的时候，它都会“生产”一个我们的 protocol 对象。
# 然后在 reactor 中安装一个 TCP监听器以等待服务请求。
# 当有请求进来时，创建一个 TSServProtocol 实例来服务那个客户。
factory = protocol.Factory()
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()


