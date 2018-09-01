## fork函数和exec函数

--------

fork是Unix中派生新进程的唯一方法

```c
#include <unistd.h>
pid_t fork(void);	//返回：子进程为0，父进程返回子进程ID，出错返回-1
```

fork有两个典型用法

> 1. 一个进程创建自身副本，这样每个副本都可以在另一个副本执行其他任务的同时处理各自的某个操作
> 2. 一个进程想执行另外一个程序。先创建新进程，然后其中一个副本（通常是子进程）调用exec把自身替换成新的程序。

存放在硬盘的__可执行程序文件__能够被__Unix执行的唯一方法__是：由一个现有进程调用六个exec函数的某一个。

> 新程序通常从main函数开始执行，进程ID不改变，称调用exec的进程为**调用进程**，称新执行的程序为**新程序**

### 6个exec函数的区别

> + 待执行的程序文件是由文件吗还是由路径名来指定
> + 新程序的参数是一一列出还是由一个指针数据来引用
> + 把调用进程的环境传递给新程序还是给新程序指定一个新环境

```c
#include <unistd.h>
int execl(const char *pathname, const char *arg0, .../* (char *)0 */);
int execv(const char *pathname, char *const *argv[]);
int execle(const char *pathname, const char *arg0, ... /* (char *)0, char *const envp[] */);
int execve(const char *pathname, char *const argv[], char *const envp[]);
int execlp(const char *filename, const char *arg0, ... /* (char *)0 */);
int execvp(const char *filename, char *const argv[]);
//均返回：成功不返回，出错返回-1
```

只有execve是内核中的系统调用。其他5个都是调用execve的库函数

| execlp |      | execl |      | execle |
| :------: | :----: | :-----: | :----: | :------: |
| ↓ 创建argv |      | ↓ 创建argv |      | ↓ 创建argv |
| **execvp** | 转换file为path -> | **execv** | 增加envp -> | **execve** |

区别：

> 1. 上3个参数字符串是一个独立参数，以空指针结束。下面3个以argv数组为参数，**这个argv数组必须含有一个用于指定其末尾的空指针**
> 2. 左列2个函数指定一个filename参数
> 3. 左两列4个函数不显式指定一个环境指针

进程在调用exec之前打开的描述符**通常**跨exec继续保持打开。本默认行为可以使用fcntl设置FD_CLOEXEC描述符标志禁止掉。

