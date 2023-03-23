import os

versions = [[3, i] for i in range(7, 12)]
print(os.getcwd())


command = 'gcc -shared -DMS_WIN64 -Ofast ' \
          '-I"/Yel/interpreters/Python{0}.{1}/include" ' \
          '-L"/Yel/interpreters/Python{0}.{1}/libs" ' \
          '-o module.cp{0}{1}-win_amd{bit}.pyd -fPIC module.c -lpython{0}{1}'

for version in versions:
    os.system(command.format(*version, bit=64))
