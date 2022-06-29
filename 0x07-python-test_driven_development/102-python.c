#include <Python.h>

/**
 * print_python_string - Print info about
 * Python string
 *
 * @p: string struct
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else if (PyUnicode_IS_COMPACT(p) && !PyUnicode_IS_ASCII(p))
			printf("  type: compact unicode object\n");
		else
			printf("  type: legacy string\n");


		printf("  length: %zu\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
		printf("  [ERROR] Invalid String Object\n");
}
