#include<stdio.h>
#include<stdlib.h>
#include<math.h>
struct node{
	int pow;
	double coe;
	struct node *next;
};

struct node *creatnode();
struct node *addnode(struct node *h1, struct node *h2);
void freenode(struct node *h);
void outputnode(struct node *h);

int main()
{
	struct node *h1, *h2;
	printf("\t\tPolynomial summation\n");
	printf("\tEnter the power and coefficient of the 1st polynomial\n");
	h1 = creatnode();
	printf("\tEnter the power and coefficient of the 2nd polynomial\n");
	h2 = creatnode();
	outputnode(h1);
	printf("+");
	outputnode(h2);
	h1 = addnode(h1, h2);
	printf("=");
	outputnode(h1);
	freenode(h1);
	freenode(h2);
	return 0;
}

struct node *creatnode()
{
	printf("Power (enter Ctrl + Z / D for end):");
	int n;
	struct node *head = NULL, *newnode, *s, *sf;
	while(scanf("%d", &n)>0)
	{
		newnode = (struct node *)malloc(sizeof(struct node));
		newnode->pow = n;
		newnode->next = NULL;
		printf("Coefficient of power %d:", n);
		scanf("%lf", &newnode->coe);
		for (s = head; s && n < s->pow; s = s->next)
			sf = s;
		if (s == head)
			head = newnode;
		else
			sf->next = newnode;
		newnode->next = s;
		printf("Power (enter Ctrl + Z / D for end):");
	}
	return head;
}

struct node *addnode(struct node *h1, struct node *h2)
{
	struct node *l = h1, *k = h2, *s, *p, *lf;
	while (k)
	{
		if (l == NULL || l->pow < k->pow)
		{
			p = (struct node *)malloc(sizeof(struct node));
			p->coe = k->coe;
			p->pow = k->pow;
			lf = lf->next = p;
			p->next = l;
			k = k->next;
		}
		else if (l->pow == k->pow)
		{
			if (l->coe + k->coe < 1e-6)
			{
				if (l == h1)
					h1 = l->next;
				else
					lf->next = l->next;
			}
			else
			{
				lf = l;
				l->coe += k->coe;
			}
			k = k->next;
			l = l->next;
		}
		else
		{
			lf = l;
			l = l->next;
		}
	}
	return h1;
}

void outputnode(struct node *h)
{	
	if (h ==NULL)
		printf("0");
	else
	{
		printf("(");
		struct node *s = h;
		for (; s; s = s->next)
		{
			if (s != h && s->coe > 1e-6)
				printf("+");
			if (s->coe < -1e-6)
				printf("-");
			if (fabs(s->coe) - 1.0 > 1e-6)
				printf("%lg", fabs(s->coe));
			if (s->pow == 1)
				printf("x");
			else if (s->pow != 0)
				printf("x^%d", s->pow);
		}
		printf(")");
	}
}

void freenode(struct node *h)
{
	struct node *p = h, *q;
	for (; p; p = q)
	{
		q = p->next;
		free(p);
	}
}
