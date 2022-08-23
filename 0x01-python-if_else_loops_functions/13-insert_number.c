#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *buffer1, *buffer2;


	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);
	newNode->n = number;

	if (*head == NULL)
	{
		*head = newNode;
	}
	else if (number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		buffer1 = *head;
		while (buffer1->next)
		{
			buffer2 = buffer1->next;
			if (number < buffer2->n)
				break;
			buffer1 = buffer1->next;
		}
		
		if (buffer1->next)
			newNode->next = buffer1->next;
		else
			newNode->next = NULL;
		buffer1->next = newNode;
	}

	return (*head);
}	
