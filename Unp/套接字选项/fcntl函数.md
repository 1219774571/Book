## fcntl函数

---

fcntl函数可执行各种描述符控制操作

```c
#include <fcntl.h>
int fcntl(int fd, int cmd, ... /*int arg*/);	//返回：若成功取决于cmd，出错-1
```

fcntl函数提供了与网络编程相关的如下特性

> - 非阻塞式I/O。通过使用**F_SETFL**命令设置**O_NONBLOCK**文件状态标志，我们可以把一个套接字设置为非阻塞型
> - 信号驱动式I/O。通过使用**F_SETFL**命令设置**O_ASYNC**文件状态标志，我们可以把一个套接字设置成一旦其状态发生变化，内核就产生一个**SIGIO**信号
> - **F_SETOWN**命令允许我们指定用于接收**SIGIO**和**SIGURG**信号的套接字属主(进程ID或进程组ID)。其中**SIGIO**信号是套接字被设置为信号驱动式I/O型后产生的，**SIGURG**信号是在新的带外数据到达套接字时产生的。**F_GETOWN**命令返回套接字的当前属主

每种描述符（包括套接字描述符）都有一组由**F_GETFL**命令获取或由**F_SETFL**命令设置的文件标志。其中影响套接字描述符的两个标志是：

O_NONBLOCK ---- 非阻塞式I/O

O_ASYNC ---- 信号驱动式I/O

> 设置某个文件状态标志的唯一正确方法是：`先取得当前标志，与新标志逻辑或后在设置标志`
>
> 指定接收信号的套接字属主为一个进程或一个进程组的差别在于：`前者仅导致单个进程接收信号，而后者则导致整个进程组中的所有进程（也许不知一个进程）接收信号`

### fcntl、ioctl和路由套接字操作小结

|              操作              |        fcntl         |  ioctl   | 路由套接字 | POSIX |
| :----------------------------: | :------------------: | :------: | :--------: | :---: |
|   设置套接字为非阻塞式I/O型    | F_SETFL , O_NONBLOCK | FIONBIO  |            | fcntl |
|  设置套接字为信号驱动式I/O型   |  F_SETFL , O_ASYNC   | FIOASYNC |            | fcntl |
|         设置套接字属主         | F_SETOWN | SIOCSPGRP或FIOSETOWN |            | fcntl |
|         获取套接字属主         | F_SETOWN | SIOCGPGRP或FIOGETOWN |            | fcntl |
| 获取套接字接收缓冲区中的字节数 |                      | FIONREAD |            |       |
|   测试套接字是否处于带外标志   |                      | SIOCATMARK |            | sockatmark |
|          获取接口列表          |                      | SIOCGIFCONF | sysctl |       |
|            接口操作            |                      | SIOC[GS]IFxxx |            |       |
|        ARP告诉缓冲操作         |                      | SIOCxARP | RTM_xxx |       |
| 路由表操作 | | SIOCxxxRT | RTM_xxx ||