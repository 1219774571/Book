## getsockopt和setgockopt函数

------

这两个函数仅限用于套接字

```c
#include <sys/socket.h>
int getsockopt(int sockfd, int level, int optname, void *optval, socklen_t *optlen);
int setsockopt(int sockfd, int level, int optname, const void *optval, socklen_t *optlen);
//均返回：成功为0，出错为-1
```

level（级别）指定系统中解释选项的代码或为通用套接字代码，或为某个特定于协议的代码

optval是一个指向某个变量的指针

> setsockopt从*optval中取得选项待设置的新值
>
> getsockopt则把以获取的选项当前值存放到*optval中
>
> *optval的大小由最后一个参数指定

#### 套接字选项粗分为两大基础类型

> 1. 启动或禁止某个特性的二元选项（称标志选项）
> 2. 取得并返回我们可以设置或检查的特定值选项（称值选项）

![传输层套接字选项](/home/coffee/Book/Unp/套接字选项/img/传输层套接字选项1.jpg)

![传输层套接字选项2](/home/coffee/Book/Unp/套接字选项/img/传输层套接字选项2.jpg)

