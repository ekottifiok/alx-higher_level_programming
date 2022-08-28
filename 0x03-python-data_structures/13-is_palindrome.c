#include "lists.h"

/**
 * add_node - adds a node pointer
 *
 * @head: the pointer to the head pointer
 * @n: the new integer
 * Return: list_t*
 */
listint_t *add_node(listint_t **head, int n)
{
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = n;
	node->next = *head;
	*head = node;
	return (*head);
}


/**
 * is_palindrome - checks if a listint_t is a palindrome
 * @head: the listint_t to be checked
 *
 * Return: 1 if it is, 0 it's not
 */
int is_palindrome(listint_t **head)
{
	listint_t *buffer1, *buffer2 = NULL;

	if (!(*head))
		return (1);
	buffer1 = *head;
	for (; buffer1; buffer1 = buffer1->next)
	{
		if (buffer2 && buffer1->n == buffer2->n)
			break;
		add_node(&buffer2, buffer1->n);
	}

	for (; buffer1 && buffer2 && buffer1->n == buffer2->n;
		 buffer1 = buffer1->next, buffer2 = buffer2->next)
		;
	if (!buffer1 && !buffer2)
		return (1);
	return (0);
}
