# shutdown函数

终止网络连接的通常方法是调用close函数。不过close有两个限制，可以使用shutdown来避免

> 1. close把描述符的引用计数减1，仅在该计数变为0时才关闭套接字。而使用shutdown可以不管引用计数就激发TCP的正常连接终止序列
> 2. close终止读和写两个方向的数据传送

```c
#include <sys/socket.h>
int shutdown(int sockfd, int howto);    //返回：成功为0，出错为-1
```

howto参数的值

> **SHUT_RD**   关闭连接的读这一半，套接字中不再有数据可接收，而且套接字接收缓冲区中的现有数据都被抛弃
>
> **SHUT_WR**   关闭连接的写这一半，对于TCP套接字，称**半关闭**。当前留在套接字发送缓冲区中的数据将被发送掉，后跟TCP的正常连接终止序列
>
> **SHUT_RDWR** 连接的读半部和写半部都关闭

## 拒绝服务型攻击

> 基本概念：当一个服务器在处理多个客户时，它绝对不能阻塞于只与单个客户相关的某个函数调用。否则可能导致服务器被挂起，拒绝为所有其他客户提供服务器，这就是**拒绝服务型攻击**
>
> 解决方法：
>
> - 使用非阻塞式I/O
> - 让每个客户由单独的控制线程提供服务（例如创建一个子进程或一个线程来服务每个客户）
> - 对I/O操作设置一个超时
