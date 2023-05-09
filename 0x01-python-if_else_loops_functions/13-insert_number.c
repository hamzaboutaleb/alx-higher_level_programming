#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in linked list sorted
 * @head: pointer to head
 * number: number
 * Return: list
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t **prev;
    listint_t **ptr;

    new_node = (listint_t *)malloc(sizeof(listint_t));

    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    if (!(*head) && !head)
        *head = new_node;

    if ((*head)->n > number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    prev = head;
    ptr = head;

    while ((*ptr)->n < number && (*ptr))
    {
        prev = ptr;
        ptr = &(*ptr)->next;
    }
    new_node->next = *ptr;
    (*prev)->next = new_node;
    return (new_node);
}
