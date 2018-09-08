# pselect函数

pselect函数是由POSIX发明的

```c
#include <sys/select.h>
#include <signal.h>
#include <time.h>
int pselect(int maxfdp1, fd_set *readset, fd_set *writeset, fd_set *exceptset, const struct timespec *timeout, const sigset_t *sigmask);
返回：若有就绪描述符则为其数目，若超时为0，出错为-1;
struct timespec{
    time_t tv_sec;   //秒
    long tv_nsec;    //纳秒
};
```

pselect和select有两个变化

> 1. pselect使用timespec结构，而不是使用timeval结构。
> 2. pselect函数增加了第六个参数：一个指向信号掩码的指针