#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - Checks for palinrome in single linked list
 * @head: head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *beg = NULL, *end = NULL;
	unsigned int length = 0, a = 0;

	if (head == NULL)
		return (0);
	beg = *head;
	end = *head;
	length = len(beg);

	for (a = 0; a < length; a += 2)
	{
		
		if (beg[a].n != end[(length * 2) - 2 - a].n)
			return (0);
	}
	return (1);
}
/**
 * len - Checks for len of linked list
 * @h: head of list
 * Return: length
 */
size_t len(listint_t *h)
{
	int count = 0;

	while (h != NULL)
	{
		h = h->next;
		count++;
	}
	return (count);
}
