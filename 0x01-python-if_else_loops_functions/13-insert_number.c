#include "lists.h"

/**
 * insert_node - Inserts a number into the linked
 * list
 *
 * @head: head node
 * @number: number to be inserted
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *str, *ptr = malloc(sizeof(listint_t));

	if (ptr == NULL)
		return (NULL);

	ptr->n = number;
	ptr->next = NULL;

	if (*head == NULL || (*head)->n >= ptr->n)
	{
		ptr->next = *head;
		*head = ptr;
	}
	else
	{
		str = *head;
		while (str->next != NULL && str->next->n < ptr->n)
		{
			str = str->next;
		}
		ptr->next = str->next;
		str->next = ptr;
	}
	return (ptr);
}
