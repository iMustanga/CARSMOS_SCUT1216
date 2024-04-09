
import logging
import os
import argparse
from argparse import RawTextHelpFormatter
# f=open('./install_requirements.txt')
source = ' -i https://pypi.doubanio.com/simple'
# source = ' -i https://pypi.tuna.tsinghua.edu.cn/simple'
# source = ' -i http://mirrors.aliyun.com/pypi/simple/  '
# opt = ' --no-index --find-links=/home/dora/workspace/simulate/team_code/dependencies/requirements/site-packages/ ' 
opt = ' '
description = "success!\n"
parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
parser.add_argument('--filename', default='./install_requirements.txt',
                        help='filename (default: ./requirements.txt)')
arguments = parser.parse_args()
print("success!!!")
print("success!!!")
f=open(arguments.filename)
fail = []
num = 0
for line in f:

    # right = line.find('git')
    # if right >0:
    #     logging.error('pip3 install '  +   line  )
    #     os.system('pip3 install '  +   line )
    #     continue
    right = line.find(';')
    if right >0:
        logging.warning('pip3 install  '  + opt+  line[:line.find(';')] + source )
        os.system('pip3 install '  +   opt + line[:line.find(';')] + source)
        continue


    if line[0] == '#' or line == '\n':
        print("无效命令！！")
        continue
    right = line.find('#')
    print('right: ',right)

    if right >0:
        logging.warning('pip3 install '  + opt +   line[:line.find(' ')]   + source)
        os.system(' pip3 install  '  +   opt +  line[:line.find(' ')] +  source  )
    elif right < 0:
        logging.warning('pip3 install '  + opt+   line[:line.find(' ')]   +source)

        # print('pip install '  +   line.strip('\n')   +' -i https://pypi.doubanio.com/simple')
        os.system('pip3 install '  + opt +   line.strip('\n') +  source  )
    # logging.warning('warning_end:***** ************************************************')
    #flag = input("是否继续安装：Enter (如果退出，请按1；如果当前库安装失败，请按2)   ")
    #if flag == "1":
    #    break;
    #elif flag == '2':
    #    fail.append(line)
        
print("安装失败库列表：",fail)





