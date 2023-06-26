#include <Python.h>

/**
 * print_python_float - prints python float
 * @p: byte
 */
void print_python_float(PyObject *p)
{
	char *s;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	s = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval,
			'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}

/**
 * print_python_bytes - prints python bytes
 * @p: byte
 */
void print_python_bytes(PyObject *p)
{
	long int size, i;
	char *trying_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	trying_str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", trying_str);
	if (size >= 10)
		printf("  first 10 bytes:");
	else
		printf("  first %ld bytes:", ++size);
	for (i = 0; i < size && i < 10; i++)
		printf(" %02hhx", trying_str[i]);
	printf("\n");
}

/**
 * print_python_list - prints python lists
 * @p: list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	int i;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		type = (((PyListObject *)p)->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}
