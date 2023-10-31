#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *pt1;
	listint_t *pt2;

	if (!list)
		return (NULL);
	pt1 = malloc(sizeof(listint_t));
	pt2 = malloc(sizeof(listint_t));

	pt2 = list->next;
	while (pt2)
	{
		pt1 = list;
		while(pt1 != pt2)
		{
			if (pt2->next == pt1)
				return (1);
			pt1 = pt1->next;
		}
		pt2 = pt2->next;
	}
	return (0);
}
