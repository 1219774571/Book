# 给一个UDP套接字多次调用connect

拥有一个已连接UDP套接字的进程可出于下列两个目的之一再次调用connect：

- 指定新的IP地址和端口号
- 端口套接字

第一个目的（即给一个已连接UDP套接字指定一个新的对端）不同于TCP套接字中connect的使用：对于TCP套接字，connect只能调用一次

为了断开一个已连接的UDP套接字，我们再次调用connect时把套接字地址结构的地址族成员设置为**AF_UNSPEC**。这样做可能会返回一个**EAFNOSUPPORT**错误，不过没关系。使套接字断开连接的是在已连接UDP套接字上调用connect的进程
