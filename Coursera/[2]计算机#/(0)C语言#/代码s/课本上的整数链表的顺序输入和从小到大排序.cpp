#include<stdio.h>
#include<malloc.h>
struct intNode
{
	int value;
	intNode *next;
};
intNode *createlist(int n)
{
	intNode *head,*tail,*p;
	int i ;
	head=tail=NULL;
	printf("Input data.\n");
	for (i=0;i<n;i++)
	{
		p=(intNode*)malloc(sizeof(intNode));//申请下一个表元的存储空间
		scanf("%d",&p->value);
		if( head==NULL) {head=tail=p;}//存储第一个表元
		else {tail=tail->next=p;}//使tail->next1指向p，而tail指向下一个新表元
	}
	if(tail){tail->next=NULL;}//保证顺序输入的末表元为空
	return head;
}

intNode *createSortlist(int n)
{
		intNode *v,*u,*p,*head;
		int i;
		head=NULL;
		printf("Input data.\n");
		for (i=0;i<n;i++)
	{
		p=(intNode*)malloc(sizeof(intNode));//申请下一个表元的存储空间
        printf("输入一个整数\n");
		scanf("%d",&p->value);
		v=head;//每次从表头开始遍历
		while(v!=NULL && p->value>v->value)//寻找新表元插入的点
		{
			u=v;v=v->next;//u指向当前表元，v继续向下遍历
		}
		if(v==head){head=p;}//在表头插入
		else {u->next=p;p->next=v;}//在中间或末尾插入	
	}
		return head;
}
	
 

void main()
{
	int n;
	intNode *q,*p,*t;
	printf("输入链表的表元个数\n");
	scanf("%d",&n);
	p=createlist(n);
	q=createSortlist(n);
	while(p)
	{
		printf("%d\t",p->value);
		t=p->next;
		free(p);
		p=t;
	}
	printf("\n");
	while(q)
	{
		printf("%d\t",q->value);
		t=q->next;
		free(q);
		q=t;
	}
}