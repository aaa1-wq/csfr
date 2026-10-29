#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct Farey {
	int a, b;
	double c;
	struct Farey *next;
};
int gcd(int a, int b)
{
	if (b)
		return gcd(b, a % b);
	return a;
}
struct Farey *initNode(int m, int n)
{
	struct Farey *p = (struct Farey *)malloc(sizeof(struct Farey));
	int q = gcd(m, n);
	p->a = m / q;
	p->b = n / q;
	p->c = m * 1.0 / n;
	p->next = NULL;
	return p;
}
void insert(struct Farey *h, struct Farey *p)
{
	struct Farey *s = h, *sf = NULL;
	while (s && p->c - s->c > 1e-6)
	{
		sf = s;
		s = s->next;
	}
	if (s == NULL || fabs(p->c - s->c) > 1e-6)
	{
		sf->next = p;
		p->next = s;
	}
}
struct Farey *makeFarey(int n)
{
	int i, j;
	struct Farey *head = initNode(0, 1), *q;
	for (i = 1; i <= n; i++)
	{
		for (j = 1; j <= i; j++)
		{
			q = initNode(j, i);
			insert(head, q);
		}
	}
	return head;
}
void outputFarey(struct Farey *head, int n)
{
	struct Farey *p = head;
	printf("Farey sequence F(%d):\n", n);
	while (p)
	{
		printf("%d/%d ", p->a, p->b);
		p = p->next;
	}
}
void freeFarey(struct Farey *h)
{
	struct Farey *p = h, *q;
	for (; p; p = q)
	{
		q = p->next;
		free(p);
	}
}
