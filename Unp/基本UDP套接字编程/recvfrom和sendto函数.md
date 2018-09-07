## recvfrom和sendto函数

---

TCP和UDP这两个传输层之间的差别：UDP是无连接不可靠的数据报协议，非常不同于TCP提供的面向连接的可靠字节流

```c
#include <sys/socket.h>
ssize_t recvfrom(int sockfd, void *buff, size_t nbytes, int flags, 
                 struct sockaddr *from, socklen_t *addrlen);
ssize_t sendto(int sockfd, const void *buff, size_t nbytes, int flags,
              struct sockaddr * to, socklen_t addrlen);	
//均返回：若成功则为读或写的字节数，出错则为-1
```

一个基本规则：对于一个UDP套接字，由它引起的异步错误却并不返回给它，除非它已连接

#### 服务器可从到达的IP数据报中获取的信息

| 来自客户的IP数据报 | TCP服务器   | UDP服务器   |
| ------------------ | ----------- | ----------- |
| 源IP地址           | accept      | recvfrom    |
| 源端口号           | accept      | recvfrom    |
| 目的IP地址         | getsockname | recvmsg     |
| 目的端口号         | getsockname | getsockname |

