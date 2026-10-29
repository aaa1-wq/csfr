#include    <stdio.h>
#include	<string.h>
#include	<stdlib.h>
#include	<time.h>
#define LIST struct link 
LIST{int data;LIST *next;};

LIST *order(LIST *h,int n)/* 形成有序链表 */
{ /* h为有序链表的表头 */
	LIST *v=h,*u,*p;//u指向上一个表元，v指向下一个表元
    //v：从首表元开始寻找插入位置
	while(v && n > v->data)//寻找插入位置
	{
		u=v;  //保存前驱表元指针，并考察下一个表元 
		v=v->next;
	} 
    p=(LIST *)malloc(sizeof(LIST));//申请看空间
	p->data = n ;	//data 存入新表元
    if(v==h)h=p;	//新表元插在首表元前
	else u->next=p; //新表元插在u所指表元后,v所指表元前
	p->next=v;    
	return h;		//返回有序链表的头指针h
}





LIST *mergesort(LIST *a,LIST *b)/*合并有序链*/
{
	LIST *c,  //工作指针
		 *d; //保留头指针
    c=(LIST *)malloc(sizeof(LIST));
	d= a->data < b->data?a:b;//保留头指针
	while( a && b)//两个链表均不为空
		if( a->data <= b->data)//a链表的值小于b链表的值
		{
			c->next=a;//a链表的当前地址放在c->next
			c=a;	  //c指向a;
			a=a->next;//取下一个
		}
		else //反之
		{
			c->next = b;
			c=b;
			b=b->next;
		}
		c->next=(a==NULL)?b:a;
		/*若其中有一个链表为空，则将不为空的链表接在当前链表的后面*/
		return d;
}

void  writelist(LIST  *head)
{
	 LIST *p=head;
	 int i=0;
	 while(p)
	 {
		 printf("%d%c",p->data,++i%10?' ':'\n');
	     p=p->next;
	 }
	 printf("\n\n");
}
	
 LIST * input(int n)
 {
	 int i,j;
	 LIST *head=NULL;
	 for(i=0;i<n;i++)
	 {
		j=rand()%100;
		printf("%d%c",j,(i+1)%10?' ':'\n');
		head=order(head,j);/*建立A有序链表*/
	 }
	 return head;
 }


void main()
 {
	 LIST *Ahead,*Bhead;
     int  i,j,n;long now;
	 srand(time(&now));
	 printf("请输入第一个链表的长度n:");
	 scanf("%d",&n);
	 printf("\n输出第一个链表随机生成的%d个数据\n",n);
	 Ahead=input(n);
	 printf("\n输出第一个有序链表的%d个数据\n",n);
     writelist(Ahead);
     printf("\n请输入第二个链表的长度n:");
	 scanf("%d",&n);
	 printf("\n输出第二个链表随机生成的%d个数据\n",n);
	 Bhead=input(n);
	 printf("\n输出第二个有序链表的%d个数据\n",n);
	 writelist(Bhead);
     Ahead=mergesort(Ahead,Bhead);/*合并有序链*/
	 printf("输出合并后的有序链\n");
     writelist(Ahead);
 }

