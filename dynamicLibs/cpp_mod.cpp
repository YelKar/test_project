#include <Python.h>
#include "vector"

// fib(fib_max_num) more than max unsigned long long number
#define trib_max_num 94
vector<unsigned long long> fib_mem;
unsigned long long trib_mem[trib_max_num];


unsigned long long _fib(int n) {
    if (fib_mem.size() > n) {
        return fib_mem[n];
    }
    if (n <= 2) {
        return 1;
    }
    unsigned long long m = _fib(n - 1) + _fib(n - 2);
    fib_mem.push_back(m);
    return m;
}


unsigned long long _trib(int n) {
    unsigned long long m = trib_mem[n];
    if (m) {
        return m;
    }
    if (n <= 2) {
        return 1;
    }
    return trib_mem[n] = _trib(n - 1) + _trib(n - 2) + _trib(n - 3);
}


PyObject* fib(PyObject*, PyObject * n) {
    int num = PyLong_AsLong(n);
    return PyLong_FromUnsignedLongLong(_fib(num));
}


PyObject* trib(PyObject*, PyObject * n) {
    int num = PyLong_AsLong(n);
    return PyLong_FromUnsignedLongLong(_trib(num));
}

static PyMethodDef module_methods[] = {
    { "fibonacci", (PyCFunction)fib, METH_O, NULL },
    { "tribonacci", (PyCFunction)trib, METH_O, NULL },
    { NULL, NULL, 0, NULL }
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "modul",
    "dsflksfjsdlf",
    0,
    module_methods
};

PyMODINIT_FUNC PyInit_cpp_mod() {
    memset(trib_mem, 0, trib_max_num*sizeof(unsigned long long));
    return PyModule_Create(&module);
}