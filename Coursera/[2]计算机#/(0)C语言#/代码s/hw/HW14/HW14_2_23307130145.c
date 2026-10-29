#include<stdio.h>
#include<stdlib.h>
#include<time.h>
struct intNode{
	int data;
	struct intNode *next;
};

struct intNode *initLink()
{
	srand(time(NULL));
	struct intNode *head = NULL, *w, *p;
	int x, i;
	for (i = 0; i < 10; i++)
	{
		x = rand() % 100;
		p = (struct intNode *)malloc(sizeof(struct intNode));
		p->data = x;
		p->next = NULL;
		if (head == NULL)
			w = head = p;
		else
			w = w->next = p;
	}
	return head;
}

void outputLink(struct intNode *head)
{
	struct intNode *s = head;
	for (; s; s = s->next)
		printf(" %d", s->data);
	printf("\n");
}

void freeLink(struct intNode *head)
{
	struct intNode *s = head, *q;
	for (; s; s = q)
	{
		q = s->next;
		free(s);
	}
}

void delMin(struct intNode *head)
{
	struct intNode *s = head, *sfront = NULL, *q = NULL, *qf = NULL;
	int min = 105;
	for (; s; s = s->next)
	{
		if (s->data < min)
		{
			min = s->data;
			q = s;
			qf = sfront;
		}
		sfront = s;
	}
	if (q == head)
		head = q->next;
	else
		qf->next = q->next;
	free(q);
}

int main()
{
	struct intNode *h;
	h = initLink();
	printf("The linked list is:\n");
	outputLink(h);
	delMin(h);
	printf("The linked list after deleting the minimum value is:\n");
	outputLink(h);
	freeLink(h);
	return 0;
}
