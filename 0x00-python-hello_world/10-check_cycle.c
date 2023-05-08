#include "lists.h"

/**
  * check_cycle - check iflist has cycle
  * @list: list to check
  * Return: 0 if no cycle 1 is cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);

	fast = list;
	slow = list;
	while (slow && fast)
	{
		if (fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
		
		if (fast == slow)
			return (1);
	}
	return (0);
}
