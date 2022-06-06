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
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	listint_t *head1 = *head;
	listint_t *head2 = (*head)->next;
	int count = 1;

	while (head1->next != NULL)
	{
		head1 = head1->next;
		count++;
	}
	head1 = *head;
	(*head)->next = NULL;

	for (int i = 1; i < count / 2; i++)
	{
		listint_t *r = head2->next;

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
