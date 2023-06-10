#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i, j, *arr;

	if (!*head)
		return (1);
	for (i = 0; temp; temp = temp->next, i++)
	{
		arr = realloc(arr, i * sizeof(int *));
		arr[i] = temp->n;
	}
	for (j = 0; j < i / 2; j++)
	{
		if (arr[j] != arr[i - j - 1])
			return (0);
	}
	return (1);
}
