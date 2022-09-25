# 每日早安推送

使用说明。

效果如图。当然，文字是可以修改的。
![5e72e89fd7ff692a0bfa62010517c0c](https://user-images.githubusercontent.com/9566402/183242263-c93517a2-5377-435d-8386-8d47252c9e07.jpg)

首先，按图搜索，测试号，进来之后微信扫码登录！
![cf7dbd4502df44765ed3506f55caea5](https://user-images.githubusercontent.com/9566402/183242272-134e37e7-718d-42dd-9ed7-fca2810e94e6.png)

按图点击 Use this template，创建到自己的仓库下！
![e6581c43572b00b12c1a82ca8d7178b](https://user-images.githubusercontent.com/9566402/183242340-2ef26c63-1ca1-420e-abd4-8672c25d61c9.png)


按下图，创建模板，设置变量，把微信公众平台上的各种字符串按说明创建到 GitHub -> Settings -> Secrets -> Actions 中。
![71bf9d11a876d23ef0f0728645a8ba0](https://user-images.githubusercontent.com/9566402/183242301-fd6ab30e-bfe5-4245-b2a9-f690184db307.png)
![381e8ee4a7c5ec6b8c09719f2c7e486](https://user-images.githubusercontent.com/9566402/183242295-4dcf06bb-2083-4883-8745-0af753ca805c.png)
![48c60750cec7adc546e0ad99e3082b3](https://user-images.githubusercontent.com/9566402/183242320-18500adc-14e5-4522-a3ad-ae19cc4479bf.png)

在项目settings里，点击左下角的secrets里面的actions，进入之后，点击new secret 添加各种属性名称和关键值![image](https://user-images.githubusercontent.com/106228529/192136040-2fa7f06d-ea74-4437-a4fc-4eaa6502e121.png)
和里面蓝色的大写变量名一样；生日格式为09-21；日期格式为2022-09-21；
添加新变量时，依赖文件也需要添加

启用自己项目下的 Action！
![image](https://user-images.githubusercontent.com/106228529/192136176-619f2aa6-e793-4573-8937-2def30c048ec.png)


如果运行出现错误，按以下方法可以看到错误
![6b0da6f44e18c2bfd94910c377d13e6](https://user-images.githubusercontent.com/9566402/183242349-1aa5ada6-2ee7-4cf9-a542-4b2dad88b8fe.png)

这个定时任务是每天早晨8点推送，也可能会延迟推送如果会编程的同学可以自己自定义一些东西～

图中的操作，除了各种英文字符串不一样，模板消息中的中文不一样，其他的应该都是一样的，不然程序跑不通的～

