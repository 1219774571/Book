# POSIX信号处理

信号就是告知某个进程发生了某个事件的通知，也称软件中断。

> 信号可以：
>
> - 由一个进程发给另一个进程(或自身)
> - 由内核发给某个进程

每个信号都有一个与之关联的处置，也称行为

> 1. 我们可以提供一个函数，只要有特定信号发生它就被调用。函数叫信号处理函数，行为叫捕获信号。__SIGKILL__和__SIGSTOP__信号是不能捕获的。函数原型为: void handler(int signo)
> 2. 我们可以把某个信号的处置决定为SIG_IGN来**忽略**它，__SIGKILL__和__SIGSTOP__信号是不能忽略的
> 3. 我们可以把某个信号的处置决定为SIG_DFL来启用它的默认处置

## signal函数

```c
#include <signal.h>
void (*signal(int sig, void (*func)(int)))(int);
int sigaction(int sig, const struct sigaction *restrict act, struct sigaction *restrict oact);
```

建立信号处置的POSIX方法就是调用sigaction函数

### POSIX信号语义

> - 一旦安装了信号处理函数，它便一直安装着
> - 在一个信号处理函数运行期间，正被递交的信号是阻塞的
> - 如果一个信号在被阻塞期间产生了一次或多次，那么该信号被解阻塞之后__通常只递交一次__，也就是说Unix信号默认是不排队的
> - 利用sigprocmask函数选择性地阻塞或接阻塞一组信号是可能的

### 处理SIGCHLD信号

僵死进程：无论何时fork子进程都得wait它们，防止变成僵死进程

### 处理被终端的系统调用

适用于慢系统调用的基本规则

> 当阻塞于某个慢系统调用的一个进程捕获某个信号且相应信号处理函数返回时，该系统调用可能返回一个__EINTR错误__

### wait和waitpid函数

调用wait来处理已终止的子进程

```c
#include <sys/wait.h>
pid_t wait(int *statloc);
pid_t waitpid(pid_t pid, int *statloc, int options); //均返回：成功则进程ID,出错则0或-1
```

网络编程可能会遇到三种情况

> 1. 当fork子进程时，必须捕获**SIGCHLD**信号
> 2. 当捕获信号时，必须处理被中断的系统调用
> 3. **SIGCHLD**的信号处理函数必须正确编写，应使用waitpid函数以免留下僵死进程
