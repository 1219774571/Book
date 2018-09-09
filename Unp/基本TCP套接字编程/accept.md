# accept函数

accept函数由TCP服务器调用，用于从**已完成连接队列**对头返回下一个已完成连接，如果队列为空，则进程被投入睡眠（假定套接字为默认的阻塞方式）

```c
#include <sys/socket.h>
int accept(int sockfd, struct sockaddr *cliaddr, socklen_t *addrlen);
//返回：成功则为非负描述符，出错为-1
```

> sockfd为**监听套接字描述符**，accept返回值是**已连接套接字描述符**，
>
> cliaddr参数是用来返回已连接的对端进程（客户）的协议地址
>
> addrlen调用前传送cliaddr套接字地址结构的长度，调用后该整数为内核存在该套接字地址结构内的确切字节数
