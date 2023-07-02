#include <Python.h>

void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);
	printf("[.] string object info\n");
	if(!PyUnicode_CheckExact(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if(PyUnicode_IS_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	len = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
