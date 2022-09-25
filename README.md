# 微信每日早安推送使用说明----参照修改版。

效果如图。文字部分是可以自定义。
![Inked微信图片_20220925171804_L11](https://user-images.githubusercontent.com/106228529/192136712-b6a823d8-7d73-4b69-9e2b-1011700720d1.jpg)


首先，按图搜索，测试号，进来之后微信扫码登录！
![cf7dbd4502df44765ed3506f55caea5](https://user-images.githubusercontent.com/9566402/183242272-134e37e7-718d-42dd-9ed7-fca2810e94e6.png)

按图点击右上角的fork，创建到自己的仓库下！
![image](https://user-images.githubusercontent.com/106228529/192136538-da8ce380-0488-4c0b-800e-7db6741edeab.png)



按下图，创建模板，设置变量，把微信公众平台上的各种字符串按说明创建到 GitHub -> Settings -> Secrets -> Actions 中。我提供了微信推送模板内容
![71bf9d11a876d23ef0f0728645a8ba0](https://user-images.githubusercontent.com/9566402/183242301-fd6ab30e-bfe5-4245-b2a9-f690184db307.png)
![381e8ee4a7c5ec6b8c09719f2c7e486](https://user-images.githubusercontent.com/9566402/183242295-4dcf06bb-2083-4883-8745-0af753ca805c.png)
![48c60750cec7adc546e0ad99e3082b3](https://user-images.githubusercontent.com/9566402/183242320-18500adc-14e5-4522-a3ad-ae19cc4479bf.png)
![image](https://user-images.githubusercontent.com/106228529/192136929-1f2c6dda-8390-4838-9c5a-b691c538bce2.png)


在项目settings里，点击左下角的secrets里面的actions，进入之后，点击new secret 添加各种属性名称和关键值!
[image](https://user-images.githubusercontent.com/106228529/192136040-2fa7f06d-ea74-4437-a4fc-4eaa6502e121.png)
和里面蓝色的大写变量名一样；生日格式为09-21；日期格式为2022-09-21；
添加新变量时，依赖文件也需要添加

启用自己项目下的 Action！
![image](https://user-images.githubusercontent.com/106228529/192136176-619f2aa6-e793-4573-8937-2def30c048ec.png)


如果运行出现错误，按以下方法可以看到错误
![6b0da6f44e18c2bfd94910c377d13e6](https://user-images.githubusercontent.com/9566402/183242349-1aa5ada6-2ee7-4cf9-a542-4b2dad88b8fe.png)

这个定时任务是每天早晨8点推送，也可能会延迟推送。如果会编程的同学可以自己自定义一些东西～

图中的操作，除了各种英文字符串不一样，模板消息中的中文不一样，其他的应该都是一样的，不然程序跑不通的～

