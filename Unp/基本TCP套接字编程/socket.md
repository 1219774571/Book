# socket函数

网络I/O一个进程必须做的第一件事就是调用socket函数

````c
#include <sys/socket.h>
int socket(int family, int type, int protocol); //返回：成则非负描述符，出错则-1
````

> family指明协议族，type指明套接字类型，protocol应设为某个协议类型常值，设为0选择系统默认值
>
> > | family | 说明 |
> > | :------: | :----: |
> > | AF_INET | IPv4协议 |
> > | AF_INET6 | IPv6协议 |
> > | AF_LOCAL | Unix域协议 |
> > | AF_ROUTE | 路由套接字 |
> > | AF_KEY | 密钥套接字 |
> >
> > | type | 说明 |
> > | :----: | :----: |
> > | SOCK_STREAM | 字节流套接字 |
> > | SOCK_DGRAM | 数据报套接字 |
> > | SOCK_SEQPACKET | 有序分组套接字 |
> > | SOCK_RAW | 原始套接字 |
> >
> > | protocol | 说明 |
> > | :--------: | :-----: |
> > | IPPROTO_TCP | TCP传输协议 |
> > | IPPROTO_UDP | UDP传输协议 |
> > | IPPROTO_SCTP | SCTP传输协议 |
> >
