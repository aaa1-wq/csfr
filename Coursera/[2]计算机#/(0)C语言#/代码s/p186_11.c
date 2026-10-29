#include   <stdio.h>
#include   <stdlib.h>
typedef  struct link 
{
	int data;
	struct link *next;
}LIST;

void travelLink(LIST *h)//输出链表
{
	LIST *p=h;
	putchar('\n');
    while(p)
	{
		printf("%4d",p->data);	//输出表元的值
		p=p->next;				//准备访问下一个表元
	}
}

LIST *makeLink()  //生成先进先出的链表
{
	LIST *h,	/*链表头指针*/
	*tail,	    /*链表尾指针*/
	*p;
	int n;
	h=tail=NULL;
	printf("请输入整数，结束输入请按字母.\n");
	while(scanf("%d",&n)==1)/*有整数输入*/
	{
		p=(LIST *)malloc(sizeof(LIST)); 
		p->data=n;
		p->next=NULL;
		if(h==NULL)h=tail=p;  //第一个节点，链表的头指针
		else tail=tail->next=p;//后继节点
	}
	return h;  //返回链表头指针
}

LIST *DeleMinVal(LIST *head)
{
	LIST *minp,*mpre,*p,*q;
	for(mpre=NULL,minp=head,q=NULL,p=head;p;q=p,p=p->next)
		if(minp->data>p->data)
		{
			 mpre=q;
  		     minp=p;
		}
	if(minp ==NULL)return 0;   //空表
	if(mpre==NULL)head=minp->next;//最小表元是头节点,调整表头
	else mpre->next=minp->next;  //其它位置
    return head;
}


void main()
{
	LIST *head;    
	head=makeLink();  //生成链表
    printf("输出原链表.\n");
	travelLink(head);
	printf("\n");
	head = DeleMinVal(head); //删除链表中的最小表元
    printf("\n\n输出删除最小表元后的链表.\n");
	travelLink(head);
	printf("\n");
}



/*输入下面的信息
1 54 76 -4 0 67
89
t
则输出以下结果：

输出原链表.

   1  54  76  -4   0  67  89


输出删除最小表元后的链表.

   1  54  76   0  67  89
*/
