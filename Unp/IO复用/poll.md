# poll函数

poll提供的功能与select类似，不过在处理流设备时，它能够提供额外的信息

```c
#include <poll.h>
int poll(struct pollfd *fdarray, unsigned long nfds, int timeout);
//返回：若有就绪描述符则为数目，超时则0，出错为-1
struct pollfd{
    int fd;
    short events;
    short revents;
};
```

events标志和revents标志的常值

|    常值    | 作为events的输入？ | 作为revents的结果？ | 说明 |
| :--------: | :----------------: | :-----------------: | :--: |
|   POLLIN   | √ | √ | 普通或优先级带数据可读 |
| POLLRDNORM | √ | √ | 普通数据可读 |
| POLLRDBAND | √ | √ | 优先级带数据可读 |
|  POLLPRI   | √ | √ | 高优先级数据可读 |
|  POLLOUT   | √ | √ | 普通数据可写 |
| POLLWRNORM | √ | √ | 普通数据可写 |
| POLLWRBAND | √ | √ | 优先级带数据可写 |
|  POLLERR   |   | √ | 发生错误 |
|  POLLHUP   |   | √ | 发生挂起 |
| POLLNVAL   |   | √ | 描述符不是一个打开的文件 |

poll设备三类数据：普通、优先级带、和高优先级

就TCP和UDP套接字而言，以下条件引起poll返回特定的revent，但定义中留了许多空洞（有多种方法可返回相同的条件）

> - 所有正规TCP数据和所有UDP数据都被认为是**普通数据**
> - TCP的带外数据被认为是**优先级带数据**
> - 当TCP连接的读半部关闭时（譬如收到了一个来自对端的FIN），也被认为是**普通数据**，随后的读操作将返回0
> - TCP连接存在错误即可认为是**普通数据**，也可认为是**错误**(POLLERR)，无论哪种读操作都将返回-1，并将errno设置成合适的值
> - 在监听套接字上有新连接可用既可认为是**普通数据**，也可认为是**优先级数据**。大多数实现视为**普通数据**
> - 非阻塞式connect的完成被认为是使相应套接字可写

结构数据中元素的个数是由nfds参数指定。

timeout参数指定poll函数返回前等待多长时间

| timeout值 |         说明         |
| :-------: | :------------------: |
|  INFTIM   |       永远等待       |
|     0     | 立刻返回，不阻塞进程 |
|    > 0    | 等待指定数据的毫秒数 |
