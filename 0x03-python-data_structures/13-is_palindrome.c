#include "lists.h"

/**
 * reverse_listint - reverses a listint
 * @head: head of listint
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if linked list is a palindome
 * @head: listint_t
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *single, *dble, *rev_head;

	if (!*head)
		return (1);
	for (single = dble = *head; dble && dble->next;
			single = single->next, dble = dble->next->next)
		;
	if (dble)
		rev_head = single->next;
	else
		rev_head = single;
	reverse_listint(&rev_head);
	for (single = *head; rev_head && single; rev_head = rev_head->next,
			single = single->next)
	{
		if (single->n != rev_head->n)
			return (0);
	}
	return (1);
}
