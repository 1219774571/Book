## ICMPv6套接字选项

这是唯一的套接字选项由ICMPv6处理，他的级别（即getsockopt和setsockopt函数中的第二个参数）为IPPROTO_ICMPV6

#### ICMP6_FILTER

本选项允许我们获取或设置某一个**icmp6_filter**结构，该结构指出256个可能的ICMPv6消息类型中哪些将经由某个原始套接字传递给所在进程