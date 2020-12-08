#include "lists.h"
/**
 * insert_node - inserts given node in sorted list
 * head: head of list
 * number: value of node
 * Return: Node Address or null
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *bigWilly = *head;
    listint_t *smallWilly = NULL;

    smallWilly = malloc(sizeof(listint_t));
    if (smallWilly == NULL)
        return (NULL);
    /* Storing Numbers in smallWily */
    smallWilly->n = number;
    smallWilly->next = NULL;
    /*If there is nothing in list */
    if (*head == NULL)
    {
        *head = smallWilly;
        smallWilly->next = NULL;
        return (smallWilly);
    }
    /* if there is one node in the list */
    if (smallWilly-> n < bigWilly->n)
    {
        *head = smallWilly;
        smallWilly->next = bigWilly;
        return (smallWilly);
    }
    /* if there is more than 1 in the list */
    while (bigWilly->next && bigWilly->next->n < number)
        bigWilly = bigWilly->next;
    smallWilly->next = bigWilly->next;
    bigWilly->next = smallWilly;
    
}
