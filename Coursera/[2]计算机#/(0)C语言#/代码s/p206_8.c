/*函数insert从指定文件读入整数，生成一个从小到大顺序链接的有序整数链表信息。
函数write输出整数和它们的个数*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct node 
{  
	int val;
	int count;
    struct node *next;
}NODE;

NODE *head = NULL;

void write()
{
	printf("\n排序后的各链表的值:\n\n");
	printf("整数值\t个数\n");
	for(;head;head=head->next)
		printf("%d\t%d\n",head->val,head->count);
	printf("\n");
}

void insert(char *fname,FILE *fp)
{  
	NODE *u,*v,*p;
	int x;
    while (fscanf(fp,"%d", &x) == 1) 
	{  
		v = head;   //从首表元开始寻找插入位置 
		p = (NODE *)malloc(sizeof( NODE));//申请看空间
		p -> val = x;
		p -> count = 1;
		while ( v && p->val > v->val )	//寻找要插入的位置
		{   u = v;					//保存前驱表元指针
			v = v->next;			//并考察下一个表元 
		}
		if( v && p->val == v->val)v->count++;
		else 
		{
			if( v == head)head = p;
		    else u->next = p;
			p->next=v;
		}
	}
}

void main()
{
    char fname[80];
	FILE *fp;
	printf("Please input file name.\n");
	gets(fname);
	if((fp=fopen(fname,"r")) == NULL )
	{
		printf("Can not open file %s.\n",fname);
		exit(0);
	}
	insert(fname,fp);
	write();
    fclose(fp);
	printf("\n\n");
	system("pause");
}