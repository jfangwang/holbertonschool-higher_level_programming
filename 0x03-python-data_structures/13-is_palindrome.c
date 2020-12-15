#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - Checks for palinrome in single linked list
 * @head: head of list
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *beg = NULL;
	unsigned int length = 0, a = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	beg = *head;
	length = len(beg);

	for (a = 0; a <= length / 2; a++)
	{
		if (getindex(*head, a) != getindex(*head, length - 1 - a))
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

	while (!h)
	{
		h = h->next;
		count++;
	}
	return (count);
}
/**
 * getindex - Gets node of given index
 * @head: head of list
 * @idx: index
 * Return: node at given index
 */
listint_t *getindex(listint_t *head, unsigned int idx)
{
	listint_t *cur = head;
	unsigned int count = 0;

	if (head != NULL)
	{
		while (cur != NULL)
		{
			if (count == idx)
				return (cur);
			cur = cur->next;
			count++;
		}
	}
	return (NULL);
}
