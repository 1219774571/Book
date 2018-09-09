# getsockname和getpeername函数

这两个函数返回与套接字关联的本地协议地址(getsockname)，或者返回与某个套接字关联的外地地址(getpeername)

```c
#include <sys/socket.h>
int getsockname(int sockfd, struct sockaddr *localaddr, socklen_t *addrlen);
int getpeername(int sockfd, struct sockaddr *peeraddr, socklen_t *addrlen);
//均返回：成则0，错则-1
```

需要这两个函数的理由

> - 在一个没有调用bind的TCP**客户**上，connect成功返回后，getsockname用于返回由内核赋予该连接的本地IP地址和本地端口号
> - 在以端口号为0调用bind后，getsockname用于返回内核赋予的本地端口号
> - getsockname可用于获取某些套接字的地址族
> - 在一个以通配IP地址调用bind的TCP**服务器**上，accept成功返回后，getsockname就可以用于返回由内核赋予该连接的本地IP地址
> - 当一个服务器是由调用个accept的某个进程通过调用exec执行程序时，它能够**获取客户身份的唯一途径**便是调用getpeername
