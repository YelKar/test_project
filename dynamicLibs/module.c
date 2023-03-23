#include <Python.h>
#include "stdio.h"


PyObject* func() {
    return PyLong_FromLong(0);
}

static PyMethodDef module_methods[] = {
    { "foo", (PyCFunction)func, METH_VARARGS, NULL },
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
    return PyModule_Create(&module);
}