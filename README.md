# Yavin

## 依赖库注意事项
* opencv-contrib-python==3.4.2.17

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

## 多进程驱动多设备运行脚本
* 使用main.py方法  
* 聚合报告路径: summary_report/*.html  

## 命令行相关
注意，执行命令行的目录为本项目所在目录，在该目录执行ls应该看到如下文件、文件夹

```
READEME.md   common   requirementes.txt  testcase
```
### 启动用例：

```
python -m airtest run testcase/start_broadcast.air --device Android://127.0.0.1:5037/50354b4659543398 --log testcase/start_broadcast.air/log/
```

```
airtest run testcase/setting.air --log log/
airtest report testcase/setting.air --log_root log/ --export ~/Downloads/ --plugin poco.utils.airtest.report
```

### 生成报告：

```
 python -m airtest report testcase/start_broadcast.air --log_root testcase/start_broadcast.air/log/ --export ~/Downloads/ --plugin poco.utils.airtest.report
```
### run.py
`python run.py -h` 查看具体用法

## 遇到adb killed问题咋办
* 遇到adb断开连接或获取不到状态  
```
airtest adb server version (40) doesn't match this client (41); killing...
```

* 把Airtest实际驱动的adb替换成和本地一样的版本即可  
```
cp ~/Library/Android/sdk/platform-tools/adb {你的项目所在路径}/Yavin/venv/lib/python3.7/site-packages/airtest/core/android/static/adb/mac/adb
```

## zk
```text
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```
```text
docker run -d \
-p 2181:2181 \
-v {your_path}/data:/data/ \
--name=zk1  \
--privileged zookeeper
```