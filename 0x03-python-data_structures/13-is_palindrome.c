#include "lists.h"

/**
 * reverseList - reversed a linked list
 * @head: pointer to the head node of the list
 * Return: reversed list
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = head;
	next = NULL;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head node of the list
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;
	listint_t *firstHalf, *secondHalf;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	slow = *head;
	fast = *head;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	secondHalf = reverseList(slow);
	firstHalf = *head;
	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
		{
			return (0);
		}
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}
