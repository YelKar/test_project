# code
### include libraries
#### You must to include Python.h
```c
#include <Python.h> 
```
### Create something
```c
PyObject* sqr(PyObject *, PyObject * n) {
    int num = PyLong_AsInt(n); 
    return PyLong_FromInt(num * num); 
} 
```
### Define module methods
```c
static PyMethodDef mod_methods[] = {
    // some methods
    {
        "square", 
        (PyCFunction)sqr, 
        METH_O, NULL 
    }, 
    { NULL, NULL, 0, NULL } 
}; 
```
### Configure module description
```c
static PyModuleDef module = {
    PyModuleDef_HEAD_INIT, 
    "module",  // module name
    "Documentation", 
    0, 
    mod_methods 
}; 
```
### Create module initialization function
***Function's name must be `PyInit_module_file_name()` where `module_file_name` must be filename of compiled module***
```
PyMODINIT_FUNC PyInit_module() {
    return PyModule_Create(&module); 
}
```

***This module must be compiled to `module.so` on Linux or `module.pyd` on windows.***

***you can also name modules `module.__pyVersion_platform__.(so/pyd)`. For example `module.cp39_win-amd64.pyd`.***


