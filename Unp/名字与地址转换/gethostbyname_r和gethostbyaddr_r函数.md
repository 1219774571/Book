# gethostbyname_r和gethostbyaddr_r函数

有两种方法可以把诸如gethostbyname之类不可重入的函数改为**可重入函数**

1. 把由不可重入函数填写并返回静态结构的做法改为由调用者分配再由可重入函数填写结构
2. 由可冲入函数调用malloc以动态分配内存空间

```c
#include <netdb.h>
struct hostent *gethostbyname_r(const char *hostname,
struct hostent *result,
char *buf, int buflen, int *h_errnop);

struct hostent *gethostbyaddr_r(const char *addr, int len, int type,
struct hostent *result,
char *buf, int buflen, int *h_errnop);
//均返回：成功则非空指针，出错则为NULL
```

> result参数指向由调用者分配并由被调用函数填写的hostent结构，成功返回时本指针同时作为函数的返回值
>
> buf参数指向由调用者分配且大小为buflen的缓冲区。该缓冲区用于规范主机名、别名指针数组、各个别名字符串、地址指针数据以及各个实际地址
>
> result指向的hostent结构中的所有指针，都指向该缓冲区内部，gethostbyname当前的实现最多能够返回35个别名指针和35个地址指针，并内部使用一个**8192**自己的缓冲区存放这些别名和地址
>
> 如果出错，错误码就通过h_errnop指针而不是全局变量h_errno返回
