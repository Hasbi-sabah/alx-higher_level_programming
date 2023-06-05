#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *single, *dble;

	if (!list)
		return (0);
	for (single = dble = list; single && dble && dble->next;)
	{
		single = single->next;
		dble = dble->next->next;
		if (single == dble)
			return (1);
	}
	return (0);
}
