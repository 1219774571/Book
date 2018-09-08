# gethostbyaddr函数

gethostbyaddr函数试图由一个二进制IP地址找到相应的主机名，与gethostbyname的行为正好相反

```c
#include <netdb.h>
struct hostent *gethostbyaddr(const char *addr, socklen_t len, int family);
//返回：成功则非空指针，出错则为NULL且设置h_errno
```

addr参数实际上不是char *类型，而是一个指向存放IPv4地址的某个in_addr结构的指针
len参数是这个结构的大小:对于IPv4地址为4，
family参数为AF_INET
