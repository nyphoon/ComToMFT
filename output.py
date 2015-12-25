# coding=UTF-8

# save result in for windows batch by set environment variables
def bat_setvar_PorF(item , isPass, filename):
    f = open(filename, 'a')
    if isPass:
        f.writelines('SET '+item+'='+'PASS'+'\n')
    else:
        f.writelines('SET '+item+'='+'FAIL'+'\n')
    f.close()

def bat_setvar_str(item , str, filename):
    f = open(filename, 'a')
    f.writelines( 'SET {}={}\n'.format(item, str) )
    f.close()
