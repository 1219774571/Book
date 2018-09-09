# getnameinfo函数

getnameinfo是getaddrinfo的互补函数，它以一个套接字地址为参数，返回描述其中的主机的一个字符串和描述其中的服务的另一个字符串

本函数以协议无关的凡是提供这些消息，也就是说，调用者不必关心存放在套接字地址结构中的协议地址的类型，因为这些细节由本函数自行处理

```c
#include <netdb.h>
int getnameinfo(const struct sockaddr *sockaddr, socklen_t addrlen,
char *host, socklen_t hostlen,
char *serv, socklen_t servlen, int flags);
//返回，成功则0，出错则非0
```

> sockaddr指向一个套接字地址结构，其中包含待转换成直观可读的字符串的协议地址
>
> addrlen是这个结构的长度。该结构及其长度通常由accept、recvfrom、getsockname或getpeername返回
>
> host和hostlen指定主机字符串，serv和servlen指定服务字符串

sock_ntop和getnameinfo的差别在于，前者不涉及DNS，只返回IP地址和端口号的一个可显示版本；后者通常尝试获取主机和服务的名字

## 用于改变getnameinfo操作flags

|常值|说明|
|:-:|:-:|
|NI_DGRAM| 数据报服务|
|NI_NAMEREQD| 若不能从地址解析出名字则返回错误|
|NI_NOFQDN| 只返回FQDN的主机名部分|
|NI_NUMERICHOST| 以数串格式返回主机字符串|
|NI_NUMERICSCOPE| 以数串格式返回范围标识字符串|
|NI_NUMERICSERV| 以数串格式返回服务字符串|
