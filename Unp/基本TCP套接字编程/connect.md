# connect函数

TCP客户用connect函数来建立与TCP服务器的连接

```c
#include <sys/socket.h>
int connect(int sockfd, const struct sockaddr *servaddr, socklen_t addrlen);
//返回：成0错-1
```

## TCP套接字调用connect出错情况

> 1. TCP客户没收到SYN分节响应，返回**ETIMEDOUT**错误
>
> 2. 若对客户的SYN响应是RST（复位），则表明服务器主机在我们指定的端口上没有进程在等待与之连接。这是**硬错误**，客户一接收到RST马上返回**ECONNREFUSED**错误
>
> > RST是TCP在发生错误时发送的一种TCP分节，产生RST的**三个条件**:
> >
> > - 目的地为某端口的SYN到达，然而该端口上没有正在监听的服务器
> > - TCP想取消一个已有连接
> > - TCP接收到一个根本不存在的连接上的分节
>
> 3. 客户发送SYN在路由引发**目的地不可达**ICMP错误，这是**软错误**，在规定时间未收到响应，把ICMP错误作为**EHOSTUNREACH**或**ENETUNREACH**错误返回给进程，以下两种情况也有可能
>
> > - 按照本地系统的转发表，根本没有到达远程系统的路径
> > - connect调用根本不等待就返回