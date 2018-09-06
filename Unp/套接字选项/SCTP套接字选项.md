## SCTP套接字选项

----

数目相对较多的SCTP套接字选项反映除SCTP为应用程序开发人员一个了较细粒度的控制能力。它们的级别（即getsockopt和setsockopt函数的第二个参数）为**IPPROTO_SCTP**

#### SCTO_ADAPTION_LAYER

本选项允许调用者获取或设置将由本端提供给对端的适配层指示

#### SCTP_ASSOCINFO

本套接字选项可用于以下三个目的地：

> 1. 获取关于某个现有关联的信息
> 2. 改变某个已有关联的参数
> 3. 为未来的关联设置默认信息

#### SCTP_AUTOCLOSE 

本套接字允许我们获取或设置一个SCTP端点的自动关闭时间

#### SCTP_DEFAULT_SEND_PARAM

希望发送大量信息且所有信息具有相同发送参数的引用进程可以使用本选项设置默认参数，从而避免使用辅助数据或执行**sctp_sendmsg**调用

#### SCTP_DISABLE_FRAGMENTS

SCTP通常把太大而不合适置于单个SCTP分组中的用户消息分割成多个DATA快。开启本选项将在发送端禁止这种欣慰

#### SCTP_EVENTS

本套接字选项允许调用者获取、开启或禁止各种SCTP通知

#### SCTP_GET_PEER_ADDR_INFO

本选项仅用于获取某个给定对端地址的相关信息，包括拥塞窗口、平滑化后的RTT和MTU等

#### SCTP_I_WANT_MAPPED_V4_ADDR

这个标志套接字选项用于为AF_INET6类型的套接字开启或禁止IPv4映射地址，其默认状态开启

#### SCTP_INITMSG

本套接字选项用于获取或设置某个SCTP套接字正在发送INIT信息时所用的默认初始参数

#### SCTP_MAXBURST

本套接字选项允许应用进程获取或设置用于分组发送的最大猝发大小。当SCTP向对端发送数据时，一次不能发送多于这个数目的分组，以免网络被分组淹没，具体的SCTP实现有两种方法应用这个限制：

> 1. 把拥塞窗口缩减为当前飞行大小加上最大猝发大小与路径MTU的乘积
> 2. 把该值作为一个独立的微观控制量，在任意一个发送机会最多只发送这个数目的分组

#### SCTP_MAXSEG

本套接字选项允许应用程序获取或设置用于SCTP分片的最大片段大小

> 最大片段大小是一个端点范围的设置，在一到多式接口中，它可能影响不止一个关联

#### SCTP_NODELAY

开启本选项将禁止SCTP的Nagle算法，默认关闭

#### SCTP_PEER_ADDR_PARAMS

本套接字选项允许应用进程获取或设置关于某个关联的对端地址的各种参数

#### SCTP_PRIMARY_ADDR

本套接字选项用于获取或设置端点所用的主目的地址。主目的地址是本端发送给对端的所有消息的默认目的地址

#### SCTP_RTOINFO

本套接字选项用于获取或设置各种RTO信息，它们既可以是关于某个给定关联的设置，也可以是用于本地端点的默认设置

#### SCTP_STATUS

本套接字选项用于获取某个SCTP关联的状态，为了方便移植，调用者应该使用sctp_opt_info函数而不是getsockopt函数。输入的结构是sctp_status结构

SCTP状态

| 常值                   | 说明                        |
| ---------------------- | --------------------------- |
| SCTP_CLOSED            | 关联已关闭                  |
| SCTP_COOKIE_WAIT       | 关联已发送INIT              |
| SCTP_COOKIE_ECHOED     | 关联已回射COOKIE            |
| SCTP_ESTABLISHED       | 关联已建立                  |
| SCTP_SHUTDOWN_PENDING  | 关联期待发送SHUTDOWN        |
| SCTP_SHUTDOWN_SENT     | 关联已发送SHUTDOWN          |
| SCTP_SHUTDOWN_RECEIVED | 关联已收到SHUTDOWN          |
| SCTP_SHUDOWN_ACK_SENT  | 关联在等待SHUTDOWN-COMPLETE |

