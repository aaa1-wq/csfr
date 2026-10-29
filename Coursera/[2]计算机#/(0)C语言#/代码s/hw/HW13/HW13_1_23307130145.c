#include<stdio.h>
#include<string.h>
struct stu{
	char name[20];
	int gr1, gr2;
	double f;
	int gr[20];
}st[20], *pst[20];
int nam, grm, grn, num;

int jud(int a);
double wo_rk(struct stu d);
void get_in();
void out_put1(int n1, int n2, int n3);
void so_rt(struct stu *p[], int n);
void out_put2(struct stu *p[], int n1);

int main()
{
	int line, i;
	get_in();
	for (i = 0; i < num; i++)
		pst[i] = &st[i];
	out_put1(nam, grm, grn);
	so_rt(pst, num);
	out_put2(pst, nam);
	return 0;
}

int jud(int a)
{
	int x = 0;
	if (a == 0)
		return 1;
	while (a)
	{
		x++;
		a /= 10;
	}
	return x;
}

double wo_rk(struct stu d)
{
	int sum = 0, i;
	for (i = 0; i < grn; i++)
		sum += d.gr[i];
	return 0.2 * d.gr1 + 0.4 * d.gr2 + 0.4 * sum / grn;
}

void get_in()
{
	printf("Enter the original records:\n");
	char a[20], x;
	int flag1 = 0, i = -1, p, n;
	nam = grm = grn = num = -1;
	while(1)
	{
		num++; 
		while(1)
		{
			i++;
			scanf("%c", &x);
			if (x == '\n')
			{
				flag1 = 1;
				break;
			}
			if (x == ' ')
			{
				a[i] = '\0';
				if (nam < i)
					nam = i;
				strcpy(st[num].name, a);
				break;
			}
			else
				a[i] = x;
		}
		if (flag1 == 1)
			return;
		i = grn = -1;
		scanf(" %d %d", &st[num].gr1, &st[num].gr2);
		grm = jud((st+num)->gr[0]) > jud((st+num)->gr[1]) ? jud((st+num)->gr[0]) : jud((st+num)->gr[1]);
		while (1)
		{
			grn++;
			scanf("%c", &x);
			if (x == '\n')
				break;
			else
			{
				scanf("%d", &p);
				if (jud(p) > grm)
					grm = jud(p);
				st[num].gr[grn] = p;
			}
		}
		st[num].f = wo_rk(st[num]);
	}
}

void out_put1(int n1, int n2, int n3)
{
	printf("All students' records:\n");
	int i, n, j, p, k;
	for(i = 0; i < num; i++)
	{
		printf("%s", st[i].name);
		n = strlen(st[i].name);
		for (j = 0; j < n1 - n; j++)
			printf(" ");
		printf(" %d", st[i].gr1);
		p = jud(st[i].gr1);
		for (k = 0; k < n2 - p; k++)
				printf(" ");
		printf(" %d", st[i].gr2);
		p = jud(st[i].gr2);
		for (k = 0; k < n2 - p; k++)
				printf(" ");
		for (j = 0; j < n3; j++)
		{
			printf(" %d", st[i].gr[j]);
			p = jud(st[i].gr[j]);
			for (k = 0; k < n2 - p; k++)
				printf(" ");
		}
		printf("\n");
	}
	printf("\n");
}

void so_rt(struct stu *p[], int n)
{
	int i, j, k;
	for (i = 1; i < n; i++)
	{
		for (j = 0; j < n - i; j++)
		{
			k = -1;
			while(1)
			{
				k++;
				if (p[j]->name[k] > p[j + 1]->name[k])
				{
					struct stu *temp;
					temp = p[j];
					p[j] = p[j + 1];
					p[j + 1] = temp;
					break;
				}
				if (p[j]->name[k] < p[j + 1]->name[k])
					break;
			}
		}
	}
}

void out_put2(struct stu *p[], int n1)
{
	printf("All students' final grades (sorted by name):\n");
	int i, j, n;
	for (i = 0; i < num; i++)
	{
		printf("%s", p[i]->name);
		n = strlen(p[i]->name);
		for (j = 0; j < n1 - n; j++)
			printf(" ");
		printf(" %.1lf\n", p[i]->f);
	}
}
