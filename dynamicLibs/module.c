#include <Python.h>
#include "stdio.h"

// fib(max_num) more than max unsigned long long number
#define max_num 94
unsigned long long mem[max_num];


unsigned long long _fib(unsigned long long n) {
    unsigned long long m = mem[n];
    if (m) {
        return m;
    }
    if (n <= 2) {
        return !!n;
    }
    return mem[n] = _fib(n - 1) + _fib(n - 2);
}


PyObject* fib(PyObject*, PyObject * n) {
    unsigned long long num = PyLong_AsUnsignedLongLong(n);
    return PyLong_FromUnsignedLongLong(_fib(num));
}

static PyMethodDef module_methods[] = {
    { "fibonacci", (PyCFunction)fib, METH_O, NULL },
    { NULL, NULL, 0, NULL }
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "modul",
    "dsflksfjsdlf",
    0,
    module_methods
};

PyMODINIT_FUNC PyInit_module() {
    memset(mem, 0, max_num*sizeof(unsigned long long));
    return PyModule_Create(&module);
}