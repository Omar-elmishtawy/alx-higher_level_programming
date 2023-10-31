#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/*
 *
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr;
	listint_t *tmp = *head;

	ptr = malloc(sizeof(listint_t));
	if (!ptr)
		return (NULL);
	ptr->n = number;
	if (tmp == NULL || tmp->n >= number)
	{
		ptr->next = tmp;
		*head = ptr;
		return (ptr);
	}
	while(tmp->next)
	{
		if (number >= tmp->next->n)
		{
			tmp = tmp->next;
		}
		else
		{
			ptr->next = tmp->next;
			tmp->next = ptr;
			break;
		}
	}
	if (tmp->next == NULL)
	{
		ptr->next = NULL;
		tmp->next = ptr;
	}

	return (ptr);
}
