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

struct intNode *copy(struct intNode *head1)
{
	struct intNode *head2 = NULL, *w, *s, *p;
	int x, i;
	for (s = head1; s; s = s->next)
	{
		p = (struct intNode *)malloc(sizeof(struct intNode));
		p->data = s->data;
		p->next = NULL;
		if (head2 == NULL)
			w = head2 = p;
		else
			w = w->next = p;
	}
	return head2;
}

struct intNode *copyReversed(struct intNode *head1)
{
	struct intNode *head2 = NULL, *s, *p;
	for (s = head1; s; s = s->next)
	{
		p = (struct intNode *)malloc(sizeof(struct intNode));
		p->data = s->data;
		p->next = head2;
		head2 = p;
	}
	return head2;
}

struct intNode *copySorted(struct intNode *head1)
{
	struct intNode *head2 = NULL, *s, *q, *qfront, *p;
	for (s = head1; s; s = s->next)
	{
		p = (struct intNode *)malloc(sizeof(struct intNode));
		p->data = s->data;
		p->next = NULL;
		q = head2;
		while (q && q->data < s->data)
		{
			qfront = q;
			q = q->next;
		}
		if (q == head2)
			head2 = p;
		else
			qfront->next = p;
		p->next = q;
	}
	return head2;
}

int main()
{
	struct intNode *h[4];
	int i;
	
	h[0] = initLink();
	h[1] = copy(h[0]);
	h[2] = copyReversed(h[0]);
	h[3] = copySorted(h[0]);
	
	char *prompt[] = {"The random list", "The copy of the 1st list", 
	"The reversed copy of the 1st list", "The sorted copy of the 1st list"};
	for(i = 0; i < 4; i++){
		printf("%s: \n", prompt[i]);
		outputLink(h[i]);
	}
		
	for(i = 0; i < 4; i++)
		freeLink(h[i]);
		
	return 0;
}
