#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints basic info about python list
 * @p: a pointer to python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	const char *type;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		type = Py_TYPE(item)->tp_name;

		printf("Element %ld: %s\n", i, type);
	}
}
