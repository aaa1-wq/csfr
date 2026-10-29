#include<stdio.h>
#include<malloc.h>
struct intNode
{
	int value;
	intNode *next1;
	intNode *next2;
};
intNode *createandSort(int n)
{
	intNode *head,*tail,*p,*h,*u,*v;
	int i ;
	h=(intNode*)malloc(sizeof(intNode));
	h->value=0000;
	head=h;
	tail=h;
	printf("Input data.\n");
	for (i=0;i<n;i++)
	{
		p=(intNode*)malloc(sizeof(intNode));//申请下一个表元的存储空间
		scanf("%d",&p->value);
		tail=tail->next1=p;//使tail->next1指向p，而tail指向下一个新表元
		u=head;v=h;//每次从表头开始遍历
		while(v!=NULL&&p->value>v->value)//寻找新表元插入的点
		{
			u=v;v=v->next2;//u指向当前表元，v继续向下遍历
		}
		u->next2=p;p->next2=v;//插入新表元	
	}
	if(tail){tail->next1=NULL;}//保证顺序输入的末表元为空
	 return head;
}
void main()
{
	int n;
	intNode *q,*p,*t;
	printf("输入链表的表元个数\n");
	scanf("%d",&n);
	p=q=createandSort(n);
	while(p)
	{
		printf("%d\t",p->value);
		t=p->next1;
		free(p);
		p=t;
	}
	printf("\n");
	while(q)
	{
		printf("%d\t",q->value);
		t=q->next2;
		free(q);
		q=t;
	}
}