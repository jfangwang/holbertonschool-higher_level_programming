#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - Checks for palinrome in single linked list
 * @head: head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr = NULL;
	unsigned int length = 0, a = 0;

	if (head == NULL)
		return (0);
	printf("REVERSE\n");
	reverse(**head);
	ptr = *head;
	for (length = 0; ptr != NULL; length++)
		ptr = ptr->next;
	ptr = *head;
	for (a = 0; a < length; a += 2)
		if (ptr[a].n != ptr[(length * 2) - 2 - a].n)
			return (0);
	return (1);
}
listint_t reverse(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *curr = *head;
	while (curr != NULL)
	{
		printf("%d\n", *curr);
		curr->next = prev
		prev = curr
		curr = curr->next;
	}
	return curr;
}
