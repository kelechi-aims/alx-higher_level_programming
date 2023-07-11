#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - prints Python strings
 * @p: python object
 * Return: nothing
 */
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("[Error] Invalid String Object\n");
		return;
	}
	Py_ssize_t length;
	const char *value;
	int type;

	type = PyUnicode_IS_COMPACT_ASCII(p) ? 1: 0;
	length = PyUnicode_GET_LENGTH(p);
	value = PyUnicode_AsUTF8(p);
	printf("[.] string object info\n");
	printf(" type: compact %s\n", type ? "ascii": "unicode object");
	printf(" length: %ld\n", length);
	printf(" value: %s\n", value);
}
