# ===================================
# build 방법 : cd build
# python setup_nlipAdmin.py build --build-exe nlipAdmin
# ===================================
from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages=['sys', 'os', 'distutils']
                    , excludes=[]
                    , include_files=['../nlipAdmin']
)

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

exe = [Executable(script='../nlipAdmin/python/onStartMain.py'
                    , base=base
                    , target_name='nlipAdmin.exe'
                    , icon='../nlipAdmin/resource/img/logo/logo_lt.ico'
)]

setup(
    name='nlipAdmin'
    , version='1.0'
    , author='hjw'
    , description='국토정보플랫폼 유지보수 관리자'
    , options=dict(build_exe=buildOptions)
    , executables=exe
)
