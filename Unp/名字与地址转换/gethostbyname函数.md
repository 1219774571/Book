# gethostbyname函数

查找主机名最基本的函数是gethostbyname

```c
#include <netdb.h>
struct hostent * gethostbyname(const char *hostname);
//返回：成功则为非空指针，出错则为NULL且设置h_errno

struct hostent{
    char *h_name;       //主机的正式主机名
    char **h_aliases;   //指向指针的指针，这个指针指向别名
    int h_addrtype;     //主机地址类型：AF_INET
    int h_length;       //地址长度：4
    char **h_addr_list; //指向指针的指针，这个指针指向IPv4的地址
};
```

gethostbyname与我们介绍过的其他套接字函数的不同之处在于：当发生错误时，它不设置errno变量，而是将全局整数变量h_errno设置成头文件<netdb.h>中定义的下列常值之一

> - HOST_NOT_FOUND;
> - TRY_AGAIN;
> - NO_RECOVERY;
> - NO_DATA(等同于NO_ADDRESS)

NO_DATA表示指定的名字有效，但是它没有A记录。只有MX几率的主机名就是这样的一个例子

