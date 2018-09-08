# bind函数

bind函数将一个本地协议地址赋予一个套接字

> 协议地址：是32位的IPv4地址或128位IPv6地址__与__16位的TCP或UDP端口号的组合

```c
#include <sys/socket.h>
int bind(int sockfd, const struct sockaddr *myaddr, socklen_t addrlen);//成0错-1
```

对于TCP，调用bind函数可以指定一个端口号，或指定一个IP地址，也可以两者都指定，还可以都不指定

> <netinet/in.h>定义的所有INADDR_常值都是安装主机字节序定义的，都应该使用htonl

从bind函数返回的一个常见错误是__EADDRINUSE__（地址已使用）