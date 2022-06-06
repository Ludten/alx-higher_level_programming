#include "lists.h"

/**
 * is_palindrome - check id a linked list
 * is a palindrome
 *
 * @head: Head node
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *head1, *head2, *r;
	int i, count = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	head1 = *head;
	head2 = (*head)->next;
	while (head1->next != NULL)
	{
		head1 = head1->next;
		count++;
	}
	head1 = *head;
	(*head)->next = NULL;

	for (i = 1; i < count / 2; i++)
	{
		r = head2->next;

		head2->next = head1;
		head1 = head2;
		head2 = r;
	}
	if (count % 2 != 0)
	{
		head2 = head2->next;
	}
	while (head1 != NULL)
	{
		if (head1->n != head2->n)
		{
			return (0);
		}
		head1 = head1->next;
		head2 = head2->next;
	}
	return (1);
}
