#include "lists.h"
#include "stdio.h"

/* is_palindrome - check if it is palindrom
 * @head : address of the head of the list
 * Return : 0 if not palindrom 1 if palindrom
 */

int is_palindrome(listint_t **head)
{
	listint_t *next = *head;
	listint_t *prev = *head;
	listint_t *temp = NULL;

	while (next != NULL && next->next != NULL)
	{
		next = next->next->next;
		prev = prev->next;
	}
	temp = prev;
	next = temp;
	prev = NULL;
	while (next)
	{
		printf("%d\n", next->n);
		next = temp->next;
		temp->next = prev;
		prev = temp;
		temp = next;
	}
	while (*head && temp)
	
	{
		if ((*head)->n == temp->n)
		{
			*head = (*head)->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	return (1);
}
