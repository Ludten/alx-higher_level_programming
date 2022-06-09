#include "Python.h"
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print info about
 * Python lists
 *
 * @p: List struct
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;
	PyListObject *input;
	PyTypeObject *typ;
	PyVarObject *var;

	if (PyList_Check(p))
	{
		input = (PyListObject *)(p);
		var = (PyVarObject *)(p);
		size = var->ob_size;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %zu\n", size);
		printf("[*] Allocated = %zu\n", input->allocated);

		if (PyList_Size(p) > 0)
		{
			for (i = 0; i < size; i++)
			{
				item = input->ob_item[i];
				typ = item->ob_type;
				printf("Element %zu: %s\n", i, typ->tp_name);
				if (strcmp(typ->tp_name, "bytes") == 0)
					print_python_bytes(input->ob_item[i]);
			}
		}
	}
}

/**
 * print_python_bytes - print bytes info about
 * Python objects
 *
 * @p: object struct
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	PyVarObject *var;
	char *str;
	PyBytesObject *byt;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		var = (PyVarObject *)(p);
		i = var->ob_size;
		byt = (PyBytesObject *)(p);
		str = byt->ob_sval;
		printf("  size: %zu\n", i);
		printf("  trying string: %s\n", str);
		if (i > 9)
			size = 10;
		else
			size = i + 1;
		printf("  first %zu bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02hhx", byt->ob_sval[i]);
			if (i == (size - 1))
				printf("\n");
			else
				printf(" ");
		}
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

