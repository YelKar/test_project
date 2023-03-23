# C

## ```.c``` -> ```.o```

### x32
```commandline
gcc -c -Ofast -I"/Yel/interpreters/Python3.11/include" -o module.o module.c
```

### x64
```commandline
gcc -c -DMS_WIN64 -Ofast -I"/Yel/interpreters/Python3.11/include" -o module.o module.c
```
## ```.o``` -> ```.pyd```

```commandline
gcc -shared -L"/Yel/interpreters/Python3.11/libs" -o module.cp311-win_amd64.pyd module.o -lpython311
```

## ```.c``` -> ```.pyd```
### x64
```commandline
gcc -shared -DMS_WIN64 -Ofast -I"/Yel/interpreters/Python3.11/include" -L"/Yel/interpreters/Python3.11/libs" -o module.pyd -fPIC module.c -lpython311
```

[//]: # (TODO for linux)