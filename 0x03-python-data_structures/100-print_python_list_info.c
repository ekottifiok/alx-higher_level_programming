#include <Python.h>

/**
 * print_python_list_info - Prints some info of a python list
 *
 * @p: python object that carries the list
 */
void print_python_list_info(PyObject *p)
{
	int obj_size, iter;
	PyObject *object;

	obj_size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", obj_size);
	printf("[*] Alocated = %d\n", ((PyListObject *)p)->allocated);
	for (iter = 0; iter < obj_size; iter++)
		printf("Element %d: %s\n", iter, Py_TYPE(object)->tp_name);
}
