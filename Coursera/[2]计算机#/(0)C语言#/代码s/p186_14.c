#include   <stdio.h>
#include   <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef struct Node
{
	int val;
	struct Node *next;
}List;

List *Ahead, *Bhead;   //全局变量

void write(List *p)//输出链表
{   
	if(!p){printf(" 有序链表集合是空集\n");return ;}
	while(p)
	{
		printf("%4d",p->val);
		p=p->next;
	}
	printf("\n");
}

List *copyLink(List *h)	/*复制出链接相同顺序的链表*/
{
	List *n,*t,*p;
	n=t=NULL;
	while(h)
	{
		p =(List *)malloc(sizeof(List));
		p->val=h->val;
		p->next=NULL;
		if(t==NULL)n=t=p;
		else t=t->next=p;
		h=h->next;
	}
	return n;
 }

void order(List *head, int num)//建立有序链表
{	
	List *v, *p,*u;
	v=u=head->next;
	for(;v&&v->val<=num;u=v,v=v->next);//寻找要插入的位置,u=v:保留当前指针	
	if(u&&u->val==num)return;//排除相等的元素
	p=(List *)malloc(sizeof(List));//p指向新申请的表元
	p->val=num;
	if(v==head->next)head->next=p;//插在表头，修改头指针
	else u->next=p;   //插入到u表元的后面，v表元的前面
	p->next=v;        //p表元的后面是v表元if(v->val==n)
} 

void Sum(List *Ahead,List *Bhead)//实现两个集合的和运算
{
	List *A,*B,*p,*s1,*s2,*w;
	s1=copyLink(Ahead);//保存Ahead链表
    s2=copyLink(Bhead);//保存Bhead链表
    p=s2->next;
    for(A=s1->next;A;A=A->next) 
		for(B=p;B;w=B,B=B->next)
		    if(B->val==A->val) 
			{
				if(p==B)p=B->next;//删除A,B链表中的重复数,修正表头
				else w->next = B->next;   
				break;
			}	
	while(p)
	{
		order(s1, p->val);//将两个有序链合并，即S1 Ｕ S2
		p=p->next;
	}
   printf("\n S1 Ｕ S2  =");
   write(s1->next);
 }

void And(List *Ahead,List *Bhead)//实现两个集合的交集运算
{
	List *A,*B,*p;
	p=(List*)malloc(sizeof(List));//申请空间
	p->next=NULL;
	for(A=Ahead->next;A;A=A->next) 
	{
		for(B=Bhead->next;B;B=B->next)
			if(B->val==A->val)	//相等，插入
			   order(p,A->val);
	}
	printf("\n S1 ∩ S2  =");
	write(p->next); 
}

void Sub(List *Ahead,List *Bhead)//实现两个集合的差运算
{
	List *A,*B,*p,*C,*t=NULL;
	C=t;
	p=(List*)malloc(sizeof(List));//申请空间
	p->next=NULL;
	for(A=Ahead;A;A=A->next)
	{
		for(B=Bhead;B&&A->val!=B->val;B=B->next);//找A集合中不等于B集合中的元素
		if(B==NULL)//A不在B中
			order(p,A->val);
	}
	printf("\n S1 - S2  =");
	write(p->next); 
}


void (*fun[])(List *Ahead,List *Bhead) = {Sum,Sub,And};


int menu(void)
{   int c;
	while (1) 
	{
         printf("\n");  //显示菜单 
	     printf("1 : 求A,B有序链表集合的和.\n");
	     printf("2 : 求A,B有序链表集合的差.\n");
	     printf("3 : 求A,B有序链表集合的交.\n");
		 printf("0 : 退出系统!\n");
	     printf("请进入你的选择.  ");
	     scanf("%d", &c);  // 输入选择 
		 if (c >=0 && c < 4 ) return c;
         printf("\n输入错误，请重新选择.\n");
		 getchar();
    }
}    

List *input(int x,int j)
{
	List *head;
	int i,y;
	head=(List *)malloc(sizeof(List));
	head->next=NULL;
	printf("随机生成%d个S%d链表\n",x,j);
	for(i=0;i<x;i++)
	{   y=rand()%100;
		printf("%d%c",y,(i+1)%10?' ':'\n');
		order(head, y);//建立有序链表
	}
	printf("\n");
	return head;
}

void main()
{
	int x;long now;
	srand(time(&now));
	printf("请输入S1链表的个数:");
	scanf("%d",&x);
	Ahead=input(x,1);//建立链表Ahead
	printf("请输入S2链表的个数:");
	scanf("%d",&x);
	Bhead=input(x,2);//建立链表Bhead
	while (1)     
	{	x = menu();
		if(x==0)break;/* 结束程序执行 */
		(*fun[x-1])(Ahead,Bhead);	
	}
}



