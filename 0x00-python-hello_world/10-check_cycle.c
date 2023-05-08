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
	do {
		fast = fast->next;
		slow = slow->next;
		if (fast->next)
			fast = fast->next;
		else
			return (0);

		if (slow == fast)
			return (1);
	} while (fast && slow);
	return (0);
}
