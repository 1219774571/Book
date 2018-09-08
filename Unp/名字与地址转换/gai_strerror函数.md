# gai_strerror函数

可由getaddrinfo返回的非0错误值的名字和含义。
gai_strerror以这些值为它的参数，返回一个指向对应的出错信息串的指针

```c
#include <netdb.h>
const char *gai_strerror(int error);
//返回：指向错误描述消息字符串的指针
```

## getaddrinfo返回的非0错误常值

| 常值 | 说明 |
| :--:| :--: |
| EAI_AGAIN | 名字解析中临时失败 |
| EAI_BADFLAGS | ai_flags的值无效 |
| EAI_FALL | 名字解析中不可恢复地失败 |
| EAI_FAMILY | 不支持ai_family |
| EAI_MEMORY | 内存分配失败 |
| EAI_NONAME | hostname或service未提供，或者不可知 |
| EAI_OVERFLOW | 用户参数缓冲区溢出(仅限getnameinfo()函数) |
| EAI_SERVICE | 不支持ai_socktype类型的service |
| EAI_SOCKTYPE | 不支持ai_socktype |
| EAI_SYSTEM | 在errno变量中有系统错误返回 |
