import env_setting
import verify
import output
import shutil

def occour( pattern, source, name, filename):
    output.bat_setvar_PorF( name, verify.occour(pattern, source), env_setting.dir_result+filename )

def equal( pattern, source, name, filename):
    output.bat_setvar_PorF( name, verify.equal(pattern, source), env_setting.dir_result+filename )

def re_match( pattern, source, name, filename):
    output.bat_setvar_PorF( name, verify.re_match(pattern, source), env_setting.dir_result+filename )

def copy( pattern, source, name, filename):
    try:
        shutil.copy( pattern, env_setting.dir_result+name)
    except IOError as description:
        env_setting.msg("copy result file fail->{}".format(description))

def dump( pattern, source, name, filename):
    output.bat_setvar_str(name , source, env_setting.dir_result+filename)
