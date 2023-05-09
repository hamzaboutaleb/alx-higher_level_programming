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
    listint_t *new_node, *ptr, *prev;

    new_node = (listint_t *)malloc(sizeof(listint_t));

    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    ptr = *head;

    while (ptr->n < number && ptr)
    {
        prev = ptr;
        ptr = ptr->next;
    }
    prev->next = new_node;
    new_node->next = ptr;

    return (new_node);
}
