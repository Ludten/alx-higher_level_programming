#include "lists.h"

/**
 * checkPal - check for palindrome recursively
 *
 * @left: head node
 * @right: ref node
 * Return: 0 or 1
 */
int checkPal(listint_t **left, listint_t *right)
{
	if (right == NULL)
	{
		return (1);
	}
	int result = checkPal(left, right->next) && ((*left)->n == right->n);
	(*left) = (*left)->next;
	return (result);
}

/**
 * is_palindrome - check id a linked list
 * is a palindrome
 *
 * @head: Head node
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	return (checkPal(head, *head));
}
