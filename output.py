# coding=UTF-8
import env_setting

# -------------------------------------------------------- shop floor
def bat_envvar(item , isPass, filename):
    f = open(env_setting.dir_result+filename, 'a')
    if isPass:
        f.writelines('SET '+item+'='+'Pass'+'\n')
    else:
        f.writelines('SET '+item+'='+'Fail'+'\n')
    f.close()
