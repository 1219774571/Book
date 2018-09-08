# accept返回前连接终止

三路握手完成后连接建立后，客户TCP却发送一个RST（复位）

> 客户调用socket和connect，一旦connect返回，就设置**SO_LINGER**套接字选项以产生这个RST，然后终止