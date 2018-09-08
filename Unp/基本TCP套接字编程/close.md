# close函数

通常Unix close函数也用来关闭套接字，并终止TCP连接

```c
#include <unistd.h>
int close(int sockfd); //返回：成功则0，出错为-1
```

close一个TCP套接字的默认行为是把这个套接字标记成已关闭，然后立即返回到调用进程

## 描述符引用计数

关闭已连接套接字知识导致相应描述符的引用计数值减1，只要引用计数值大于0，这个close调用并不会引发
TCP的四分组连接终止序列