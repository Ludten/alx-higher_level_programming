#include <Python.h>
#include <string.h>
#include <float.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

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

	dprintf(1, "[*] Python list info\n");
	if (PyList_Check(p))
	{
		input = (PyListObject *)(p);
		var = (PyVarObject *)(p);
		size = var->ob_size;
		dprintf(1, "[*] Size of the Python List = %zu\n", size);
		dprintf(1, "[*] Allocated = %zu\n", input->allocated);

		if (size > 0)
		{
			for (i = 0; i < size; i++)
			{
				item = input->ob_item[i];
				typ = item->ob_type;
				dprintf(1, "Element %zu: %s\n", i, typ->tp_name);
				if (strcmp(typ->tp_name, "bytes") == 0)
					print_python_bytes(input->ob_item[i]);
				if (strcmp(typ->tp_name, "float") == 0)
					print_python_float(input->ob_item[i]);
			}
		}
	}
	else
		dprintf(1, "  [ERROR] Invalid List Object\n");
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
		dprintf(1, "  size: %zu\n", i);
		dprintf(1, "  trying string: %s\n", str);
		if (i > 9)
			size = 10;
		else
			size = i + 1;
		printf("  first %zu bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02hhx", byt->ob_sval[i]);
			if (i == (size - 1))
				dprintf(1, "\n");
			else
				dprintf(1, " ");
		}
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

void print_python_float(PyObject *p)
{
	PyFloatObject *flo;
	double val;
	char *str;

	dprintf(1, "[.] float object info\n");
	if (PyFloat_Check(p))
	{
		flo = (PyFloatObject *)(p);
		val = flo->ob_fval;
		str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", str);
    	}
	else
	{
		dprintf(1, "  [ERROR] Invalid Float Object\n");
	}
}
