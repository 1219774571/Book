# syslog函数

既然守护进程没有控制终端，它们就不能把消息fprintf到stderr上，从守护进程中登记消息的常用技巧就是调用syslog函数

```c
#include <syslog.h>
void syslog(int priority, const char *message, ...);
```

本函数的priority参数是**级别(level)**和**设施(facility)**两者的结合

message参数类似printf的格式串，不过增设了%m规范，它将被替换成与当前errno值对应的出错消息

## 日志消息的level可以是0-7,默认为LOG_NOTICE

| level | 值 | 说明 |
| :---: | :-:| :--:|
|LOG_EMERG| 0| 系统不可用(最高级别)|
|LOG_ALERT| 1 | 必须立即采取行动 |
|LOG_CRIT| 2 | 临界条件|
|LOG_ERR| 3 | 出错条件|
|LOG_WARNING| 4 | 警告条件 |
|LOG_NOTICE | 5 | 正常然而重要的条件(默认值) |
|LOG_INFO | 6 | 通告消息|
|LOG_DEBUF | 7 | 调式级消息(最低优先级)|

## 日志消息还包含一个用于标识消息发送进程类型facility,默认值为LOG_USER

| facility | 说明 |
| :------: | :--:|
|LOG_AUTH | 安全/授权消息|
|LOG_AUTHPRIV| 安全/授权消息(私用)|
|LOG_CRON| cron守护进程|
|LOG_DAEMON|系统守护进程|
|LOG_FTP | FTP守护进程|
|LOG_KERN | 内核消息|
|LOG_LOCAL0 | 本地使用 |
|LOG_LOCAL1 | 本地使用 |
|LOG_LOCAL2 | 本地使用 |
|LOG_LOCAL3 | 本地使用 |
|LOG_LOCAL4 | 本地使用 |
|LOG_LOCAL5 | 本地使用 |
|LOG_LOCAL6 | 本地使用 |
|LOG_LOCAL7 | 本地使用 |
|LOG_LRR | 行式打印机系统|
|LOG_MAIL | 邮件系统 |
|LOG_NEWS | 网络新闻系统 |
|LOG_SYSLOG | 由syslogd内部产生的消息 |
|LOG_USER | 任意的用户级消息(默认) |
|LOG_UUCP | UUCP系统

> 当syslog被应用进程首次调用时，它就创建一个Unix域数据报套接字，然后调用connect连接到由syslogd守护进程创建的Unix域数据报套接字的众所周知路径名,这个套接字一直保持打开，知道进程终止为止。

### 作为替换，进程也可以调用openlog和closelog

```c
#include <syslog.h>
void openlog(const char *ident, int options, int facility);
void closelog(void);
```

> openlog可以在首次调用syslog前调用，closelog可以在应用程序不再需要发送 日志消息时调用。

ident参数是一个由syslog冠于每个日志消息之前的字符串，它的值通常是程序名

options参数由一个或多个常量的逻辑或构成

| options | 说明 |
| :-----: | :--: |
| LOG_CONS | 若无法发送到syslogd守护进程则登记到控制台
| LOG_NDELAY | 不延迟打开，立即创建套接字 |
| LOG_PERROR | 既发送到syslogd守护进程，又登记到标准错误输出 |
| LOG_PID | 随每个日志消息登记进程ID |
