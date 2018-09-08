# getaddrinfo函数

getaddrinfo函数能够处理名字到地址以及服务到端口这两种转换，返回的是一个sockaddr结构而不是一个地址列表

## 注：getaddrinfo函数返回的存储空间是动态获取的，这些存储空间通告调用freeaddrinfo返回给系统

```c
#include <netdb.h>
int getaddrinfo(const char *hostname, const char *service,
                const struct addrinfo *hints, struct addrinfo ** result);
//返回：成功则0，出错则非0

struct addrinfo{
    int ai_flags;           //AI_PASSIVE, AI_CANONNAMEptr to cannonical name for host
    int ai_family;          //AF_xxx
    int ai_socktype;        //SOCK_xxx
    int ai_protocol;        //0 or IPPROTO_xxx for IPv4 and IPv6
    socklen_t ai_addrlen;   //ai_addr的长度
    char *ai_canonname;     //指向主机的规范名称的指针
    struct sockaddr *ai_addr//指向套接字地址结构的指针
    struct addrinfo *ai_next//指向链表的下一个节点
};
```

hostname参数是一个主机名或地址串(IPv4的点分十进制数串或IPv6的十六进制数串)
service 参数是一个服务名或十进制端口号数串
hints   参数可以是一个空指针，也可以是一个指向某个addrinfo结构的指针调用者在这个结构中填入关于期望返回的信息类型的暗示
> hints结构中调用者可以设置的成员有：
> - ai_flags(零个或多个或在一起的AI_xxx值)
> - ai_family(某个AF_xxx值)
> - ai_socktype(某个SOCK_xxx值)

其中ai_flags成员可用的标志值及其含义
> AI_PASSIVE    套接字将用于被动打开
>
> AI_CANONNAME  告知getaddrinfo函数返回主机的规范名字
>
> AI_NUMERICHOST防止任何类型的名字到**地址**映射，hostname参数必须是一个地址串
>
> AI_NUMERICSERV防止任何类型的名字到**服务**映射,service参数必须是一个十进制端口号数串
>
> AI_V4MAPPED   如果同时指定ai_family成员的值为AF_INET6,那么如果没有可用的AAAA记录，就返回与A记录对应的IPv4映射的IPv6地址
>
> AI_ALL        如果同时指定AI_V4MAPPED标志，那么除了返回与AAAA记录对应的IPv6地址外，还返回与AAAA几率对应的IPv6地址外，还返回与A记录对应的IPv4映射的IPv6地址
>
> AI_ADDRCONFIG 按照所处主机的配置选择返回地址类型，也就是只查找与所在主回馈接口以外的网络接口配置的IP地址版本一致的地址

|               | 服务以名字标识，它的提供者为：| ||||||
| :-----------: | :----:| :---: | :----: | :-----:  | :------:  | :-------------:| :-----------:   |
|ai_socktype暗示| 仅TCP | 仅UDP | 仅SCTP | TCP和UDP | TCP和SCTP | TCP、UDP和SCTP | 服务以端口号标识|
|   0           | 1     | 1     | 1      |  2       |   2       |   3            |  错误           |
|SOCK_STREAM    | 1     |错误   | 1      | 1        |   2       |  2             |  2              |
|SOCK_DGRAM     |错误|1|错误|1|错误|1|1|
|SOCK_SEQPACKET |错误|错误|1|错误|1|1|1|
