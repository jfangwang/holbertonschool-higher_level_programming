#include "lists.h"
/**
 * check_cycle - checks if the linked list is a loop
 * @willy: A struct pointing to a list
 * Return: 0
 */
int check_cycle(listint_t *willy)
{
	listint_t *ptr_1 = willy;
	/*Will increment by 1 */
	listint_t *ptr_2 = willy;
	/*Will increment by 2 */
	if (!willy)
		return (0);
	if (ptr_1 == ptr_1->next)
		return (0);
	while (ptr_2 && ptr_2->next)
	{
		ptr_1 = ptr_1->next;
		ptr_2 = ptr_2->next->next;
		if (ptr_1 == ptr_2)
			return (1);
	}
	return (0);
}
