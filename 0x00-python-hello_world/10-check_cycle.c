#include "lists.h"

/**
 * check_cycle - check_cycle
 * @list: list
 *
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *pt1 = list;
	listint_t *pt2 = list;

	while (pt2 != NULL && pt2->next != NULL)
	{
		pt1 = pt1->next;
		pt2 = pt2->next->next;

		if (pt1 == pt2)
			return (1);
	}
	return (0);
}

