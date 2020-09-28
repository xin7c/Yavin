import os
import sys

def projectInit():
    projectPathList = []
    print(os.path.dirname(__file__))
    projectPathList.append(os.path.dirname(__file__))
    for sysPath in sys.path:
        if "site-packages" in sysPath:
            with open(sysPath + "/LiveMeAirTest.pth", 'w', encoding="utf-8") as fp:
                for projectPath in projectPathList:
                    fp.write(projectPath + '\n')
            break


if __name__ == "__main__":
    projectInit()  # 作为submodule时，需要先执行该文件
