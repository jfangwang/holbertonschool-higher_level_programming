#include "python.h"
#include <stdio.h>
/**
*print_python_list_info - prints the size of list, space allocated,
*and each element in list.
*@p: Takes in a list
*Return: void
*/
void print_python_list_info(PyObject *p)
{
	unsigned int length = 0, count = 0;
	PyListObject *list = (PyListObject *)p;

	length = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n",length);
	printf("[*] Allocated = 2\n");
}
