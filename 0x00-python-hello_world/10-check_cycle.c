#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the list
 *
 * @list: sample list to check
 * Return: 0 for success and 1 for failure
 */
int check_cycle(listint_t *list)
{
    listint_t *buffer;

    if (list)
    {
        for (buffer = list->next; buffer; buffer = buffer->next)
    {
        if (buffer == list)
            return (1);
    }
    }

    return (0);
}
