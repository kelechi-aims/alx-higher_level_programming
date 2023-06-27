#include <Python.h>
#include <stdio.h>


void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
/**
 * print_python_list - prints some basic info about Python list
 * @p: PylistObject
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;	

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf(" [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}
	size = PyObject_Length(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		if (PyFloat_Check(item))
			print_python_float(item);
	}
	setbuf(stdout, NULL);
}

/**
 * print_python_bytes - prints basic info about Python bytes
 * @: PyObject
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i, bound;
	char *bytes;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object");
		setbuf(stdout, NULL);
		return;
	}
	size = ((PyVarObject *)(p))->ob_size;
	bytes = ((PyBytesObject *)p)->ob_sval;
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", bytes);
	if (size >= 10)
		bound = 10;
	else
		bound = size + 1;
	printf(" first %ld bytes:", bound);
	for (i = 0; i < bound; i++)
	{
		printf(" %02x", (unsigned char)bytes[i]);
	}
	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - prints basic ifo about Python float
 * @p: PyObject
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	double value;
	char *flt;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf(" [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}
	value = ((PyFloatObject *)(p))->ob_fval;
	flt = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);
	printf(" value: %s\n", flt);
	setbuf(stdout, NULL);
}
