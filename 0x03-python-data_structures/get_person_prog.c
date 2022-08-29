#include <python3.4m/Python.h>
#include <stdio.h>

extern PyObject * get_details(); // Ought to be put in a header

int main(void)
{
    PyObject * pyobj = get_details();
    if (pyobj) {
        puts("Got the details");
    }
    return  0;
}

