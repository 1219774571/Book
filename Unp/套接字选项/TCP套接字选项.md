# TCP套接字选项

-----

TCP有两个套接字选项，它们的级别（即getsockopt和setsockopt函数的第二个参数）为**IPPROTO_TCP**

## TCP_MAXSEG

本选项允许我们获取或设置TCP连接的最大分节大小（MSS）。返回值是我们的TCP可以发送给对端的最大数据量，它通常是由对端使用SYN分节通知的MSS，除非我们的TCP选择使用一个比对端通告的MSS小些的值。如果该值在相应套接字的连接建立之前取得，那么返回值是未从对端收到MSS选项情况下所用的默认值

### TCP_NODELAY

开启本选项将禁止TCP的Nagle算法，默认开启