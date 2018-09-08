# freeaddrinfo函数

由getaddrinfo返回的所有存储空间都是动态获取的(譬如来自malloc调用),包括addrinfo结构、ai_addr结构和ai_cannoname字符串

## 这些存储空间通过调用freeaddrinfo返回给系统

```c
#include <netdb.h>
void freeaddrinfo(struct addrinfo *ai);
```

ai参数应指向由getaddrinfo返回的第一个addrinfo结构