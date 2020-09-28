# Yavin

## 用例书写规范
* 公共部分放到 Common 文件夹下，比如登录，打开、关闭、清理app等
* 用例都放到 testcase 目录下，每个用例一个单独的文件夹，文件夹名称必须是.air结尾的
* 用例文件夹（即.air的文件夹）下必须有一个跟文件夹同名的 py 文件，该文件封装了整个用例的全部操作以及断言
* 用例文件里可以定义函数，类。但运行用例的语句请直接写，不要放到 `if __name__ == '__main__:'` 里面
	
## 支持链式调用
实例化子页面后，可以在子页面实例上通过`.`调用同一子页面上的方法：
```
sp1 = SettingPage()
print(Config.get_yaml().get("package_name", None))
sp1.setting_page_instance().snap("after instance").restart_app().snap("重启啦")
```

### BasePage作为父类封装的方法
* screen_size：获取当前屏幕尺寸
* snap：截图
* go_me_page：跳转个人页
* back：后退


## 命令行相关
注意，执行命令行的目录为本项目所在目录，在该目录执行ls应该看到如下文件、文件夹

```
READEME.md   common   requirementes.txt  testcase
```
启动用例：

```
python -m airtest run testcase/start_broadcast.air --device Android://127.0.0.1:5037/50354b4659543398 --log testcase/start_broadcast.air/log/
```

```
airtest run testcase/setting.air
airtest report testcase/setting.air --log_root log/ --export ~/Downloads/ --plugin poco.utils.airtest.report
```

生成报告：

```
 python -m airtest report testcase/start_broadcast.air --log_root testcase/start_broadcast.air/log/ --export ~/Downloads/ --plugin poco.utils.airtest.report
```