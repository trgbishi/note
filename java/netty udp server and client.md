#### 说明 
[代码来源](https://blog.csdn.net/fenglongmiao/article/details/79219959)

#### NettyUdpServer.java
``` java
import io.netty.bootstrap.Bootstrap;
import io.netty.channel.Channel;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioDatagramChannel;
 
/**
 * 	 <B>说	明<B/>:UdpServer
 * 
 * @author 作者名：冯龙淼
 * 		   E-mail：fenglongmiao@vrvmail.com.cn
 * 
 * @version 版   本  号：1.0.<br/>
 *          创建时间：2018年1月8日 上午10:03:38
 */
public class NettyUdpServer {
 
	private final Bootstrap bootstrap;
	private final NioEventLoopGroup acceptGroup;
	private Channel channel;
	public void start(String host,int port) throws Exception{
        try {
        	channel = bootstrap.bind(host, port).sync().channel();
        	System.out.println("UdpServer start success"+port);
        	channel.closeFuture().await();
        } finally {
            acceptGroup.shutdownGracefully();
        }
	}
	
	public Channel getChannel(){
		return channel;
	}
	
	public static UdpServer getInstance(){
		return UdpServerHolder.INSTANCE;
	}
	
	private static final class UdpServerHolder{
		static final UdpServer INSTANCE = new UdpServer();
	}
	
	private UdpServer(){
		bootstrap = new Bootstrap();
		acceptGroup = new NioEventLoopGroup();
		bootstrap.group(acceptGroup)
        .channel(NioDatagramChannel.class)
        .option(ChannelOption.SO_BROADCAST, true)
        .handler(new ChannelInitializer<NioDatagramChannel>() {
			@Override
			protected void initChannel(NioDatagramChannel ch)
					throws Exception {
				ChannelPipeline pipeline = ch.pipeline();
				pipeline.addLast(new UdpServerHandler());
			}
		});
	}
}
```

#### UdpServerHandler.java
```java

import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.channel.socket.DatagramPacket;
 
import org.apache.log4j.Logger;
 
/**
 * 	 <B>说	明<B/>:
 * 
 * @author 作者名：冯龙淼
 * 		   E-mail：fenglongmiao@vrvmail.com.cn
 * 
 * @version 版   本  号：1.0.<br/>
 *          创建时间：2018年1月8日 上午10:09:47
 */
public class UdpServerHandler extends SimpleChannelInboundHandler<DatagramPacket>{
 
	private static final Logger logger = Logger.getLogger(UdpServerHandler.class);
	
	@Override
	protected void channelRead0(ChannelHandlerContext ctx, DatagramPacket msg)
			throws Exception {
		// 接受client的消息
		logger.info("开始接收来自client的数据");
		final ByteBuf buf = msg.content();
    	int readableBytes = buf.readableBytes();
    	byte[] content = new byte[readableBytes];
	    buf.readBytes(content);
	    String clientMessage = new String(content,"UTF-8");
		logger.info("clientMessage is: "+clientMessage);
		if(clientMessage.contains("UdpServer")){
			ctx.writeAndFlush(new DatagramPacket(Unpooled.wrappedBuffer("helloClient".getBytes()),msg.sender()));
		}
	}
}
```

#### NettyUdpClient.java
```java
import io.netty.bootstrap.Bootstrap;
import io.netty.channel.Channel;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelOption;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioDatagramChannel;
 
import java.nio.charset.Charset;
 
/**
 * 	 <B>说	明<B/>:LogPush UDP client
 * 
 * @author 作者名：冯龙淼
 * 		   E-mail：fenglongmiao@vrvmail.com.cn
 * 
 * @version 版   本  号：1.0.<br/>
 *          创建时间：2017年12月28日 下午3:37:53
 */
public class NettyUdpClient {
	
	private final Bootstrap bootstrap;
	public final NioEventLoopGroup workerGroup;
	public static Channel channel;
	private static final Charset ASCII = Charset.forName("ASCII"); 
	
	public void start() throws Exception{
        try {
        	channel = bootstrap.bind(1234).sync().channel();
        	channel.closeFuture().await(1000);
        } finally {
//        	workerGroup.shutdownGracefully();
        }
	}
	
	public Channel getChannel(){
		return channel;
	}
	
	public static LogPushUdpClient getInstance(){
		return logPushUdpClient.INSTANCE;
	}
	
	private static final class logPushUdpClient{
		static final LogPushUdpClient INSTANCE = new LogPushUdpClient();
	}
	
	private LogPushUdpClient(){
		bootstrap = new Bootstrap();
		workerGroup = new NioEventLoopGroup();
		bootstrap.group(workerGroup)
        .channel(NioDatagramChannel.class)
        .option(ChannelOption.SO_BROADCAST, true)
        .handler(new ChannelInitializer<NioDatagramChannel>() {
			@Override
			protected void initChannel(NioDatagramChannel ch)throws Exception {
				ChannelPipeline pipeline = ch.pipeline();
//				pipeline.addLast(new StringDecoder(ASCII))  
//                .addLast(new StringEncoder(ASCII))
				pipeline.addLast(new LogPushUdpClientHandler());
			}
		});
	}
	
}
```


#### ClientHandler.java
``` java
import io.netty.buffer.ByteBuf;
import io.netty.buffer.Unpooled;
import io.netty.channel.Channel;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.channel.socket.DatagramPacket;
import io.netty.util.concurrent.GenericFutureListener;
 
import java.net.InetSocketAddress;
import java.nio.charset.Charset;
import java.util.List;
 
import org.apache.log4j.Logger;
 
/**
 * 	 <B>说	明<B/>:
 * 
 * @author 作者名：冯龙淼
 * 		   E-mail：fenglongmiao@vrvmail.com.cn
 *
 * @version 版   本  号：1.0.<br/>
 *          创建时间：2017年12月21日 下午4:20:49
 */
public class ClientHandler extends SimpleChannelInboundHandler<DatagramPacket>{
 
	private static final Logger logger = Logger.getLogger(LogPushUdpClientHandler.class);
	
//	private static Channel channel = LogPushUdpClient.getInstance().getChannel();
	
	@Override  
    public void channelActive(ChannelHandlerContext ctx) throws Exception {  
        //当channel就绪后。  
       logger.info("client channel is ready!");  
//       ctx.writeAndFlush("started");//阻塞直到发送完毕  这一块可以去掉的 
//       NettyUdpClientHandler.sendMessage("你好UdpServer", new InetSocketAddress("127.0.0.1",8888));
//       sendMessageWithInetAddressList(message);
//       logger.info("client send message is: 你好UdpServer");
    }
	
	@Override
	protected void channelRead0(ChannelHandlerContext ctx, DatagramPacket packet)
			throws Exception {
		// TODO 不确定服务端是否有response 所以暂时先不用处理
		final ByteBuf buf = packet.content();
    	int readableBytes = buf.readableBytes();
    	byte[] content = new byte[readableBytes];
	    buf.readBytes(content);
	    String serverMessage = new String(content);
		logger.info("reserveServerResponse is: "+serverMessage);
	}
 
	
	
	/**
	 * 向服务器发送消息
	 * @param msg 按规则拼接的消息串
	 * @param inetSocketAddress 目标服务器地址
	 */
	public static void sendMessage(final String msg,final InetSocketAddress inetSocketAddress){
		if(msg == null){
			throw new NullPointerException("msg is null");
		}
		// TODO 这一块的msg需要做处理 字符集转换和Bytebuf缓冲区
		senderInternal(datagramPacket(msg, inetSocketAddress));
	}
	
	/**
	 * 发送数据包并监听结果
	 * @param datagramPacket
	 */
	public static void senderInternal(final DatagramPacket datagramPacket,List<Channel> channelList) {
		for (Channel channel : NettyTCPClient.channelList) {
			if(channel != null){
				channel.writeAndFlush(datagramPacket).addListener(new GenericFutureListener<ChannelFuture>() {
					@Override
					public void operationComplete(ChannelFuture future)
							throws Exception {
						boolean success = future.isSuccess();
						if(logger.isInfoEnabled()){
							logger.info("Sender datagramPacket result : "+success);
						}
					}
				});
			}
		}
	}
	
	/**
	 * 组装数据包
	 * @param msg 消息串
	 * @param inetSocketAddress 服务器地址
	 * @return DatagramPacket
	 */
	private static DatagramPacket datagramPacket(String msg, InetSocketAddress inetSocketAddress){
		ByteBuf dataBuf = Unpooled.copiedBuffer(msg,Charset.forName("UTF-8"));
		DatagramPacket datagramPacket = new DatagramPacket(dataBuf, inetSocketAddress);
		return datagramPacket;
	}
	
	/**
	 * 发送数据包服务器无返回结果
	 * @param datagramPacket
	 */
	private static void senderInternal(final DatagramPacket datagramPacket) {
		logger.info("LogPushUdpClient.channel"+LogPushUdpClient.channel);
		if(LogPushUdpClient.channel != null){
			LogPushUdpClient.channel.writeAndFlush(datagramPacket).addListener(new GenericFutureListener<ChannelFuture>() {
				@Override
				public void operationComplete(ChannelFuture future)
						throws Exception {
					boolean success = future.isSuccess();
					if(logger.isInfoEnabled()){
						logger.info("Sender datagramPacket result : "+success);
					}
				}
			});
		}else{
			throw new NullPointerException("channel is null");
		}
	}
	
}
```


#### Test.java
``` java
import java.net.InetSocketAddress;
 
import org.apache.log4j.Logger;
import org.junit.Test;
 
 
/**
 * 	 <B>说	明<B/>:
 * 
 * @author 作者名：冯龙淼
 * 		   E-mail：fenglongmiao@vrvmail.com.cn
 * 
 * @version 版   本  号：1.0.<br/>
 *          创建时间：2018年1月8日 上午10:25:21
 */
public class Test {
 
	private static final Logger logger = Logger.getLogger(UdpServerMainTest.class);
	
	private static final String host = "192.168.133.72";
	
	private static final int port = 888;
	
	public static void main(String[] args) {
		try {
			UdpServer.getInstance().start(host, port);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	@Test
	public void logPushSendTest() throws Exception{
		LogPushUdpClient.getInstance().start();
		int i = 0;
		while( i < 10){
			LogPushUdpClientHandler.sendMessage(new String("你好UdpServer"), new InetSocketAddress(host,port));
		    logger.info(i+" client send message is: 你好UdpServer");
		    i++;
		}
	}
	
}
```