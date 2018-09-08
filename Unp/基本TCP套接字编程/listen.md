# listen函数

listen仅由TCP服务器调用

> listen函数把一个未连接的套接字转换成一个__被动套接字__，指示内核应接受指向该套接字的连接请求。调用listen导致套接字从__CLOSED__状态转换到__LISTEN__状态

第二个参数规定内核应该为相应套接字排队的__最大连接个数__

```c
#include <sys/socket.h>
int listen(int sockfd, int backlog); //返回：成功0，出错-1
```

## 内核为监听套接字维护两个队列

1. 未完成连接队列：客户到达服务器，服务器正在处理其他相应的TCP三路握手。这些套接字处于__SYN_RCVD__状态
2. 已完成连接队列：完成TCP三路握手，这些套接字处于__ESTABLISHED__状态
