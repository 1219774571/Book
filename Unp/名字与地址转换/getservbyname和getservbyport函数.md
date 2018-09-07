## getservbyname和getservbyport函数
---
getservbyname函数用于根据给定名字查找相应服务
```c
#include <netdb.h>
struct servent *genservbyname(const char *servname, const char *protoname);
//返回:成功非空指针，出错则为NULL

struct servent{
    char *s_name;   //规范服务名字
    char **s_aliases;   //别名列表
    int s_port;     //端口号，网络字节顺序
    char *s_porto;  //使用的协议
};
```
服务名servname参数必须指定
protoname协议名

#### getservbyport用于根据给定端口号和可选协议查找相应服务
```c
#include <netdb.h>
struct servent *getservbyport(int port, const char *pathname);
//返回：成功则为非空指针，出错则为NULL
```
port参数的值必须是网络字节序
