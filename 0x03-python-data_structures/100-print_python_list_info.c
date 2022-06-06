#include "Python.h"

/**
 * print_python_list_info - Print info about
 * Python lists
 *
 * @p: List struct
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	PyObject *item;
	PyListObject *input;
	PyTypeObject *typ;

	if (PyList_Check(p))
	{
		input = (PyListObject *)(p);
		printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
		printf("[*] Allocated = %zu\n", input->allocated);

		if (PyList_Size(p) > 0)
		{
			for (i = 0; i < PyList_Size(p); i++)
			{
				item = PyList_GetItem(p, i);
				typ = item->ob_type;
				printf("Element %zu: %s\n", i, typ->tp_name);
			}
		}
	}
}

