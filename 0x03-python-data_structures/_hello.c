#include <Python.h>

static PyObject* _hello_world(PyObject* self) {
    return PyUnicode_FromString("hello world");
}

