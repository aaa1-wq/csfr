//链表创建、插、删、填倒示意程序。  
 #include  <stdio.h>
 #include <stdlib.h>
 struct intNode /* 整数链表表元类型 */
 { 
      int value; /* 存放整数 */
      struct intNode *next; /* 存放后继表元的指针 */
 };

struct intNode *root; /* 遍历链表 */
void travelLink(struct intNode *h)
{  
	struct intNode *p = h;
    while ( p != NULL ) 
	{  
        printf("%4d ", p->value); /* 输出表元的值 */
        p = p->next;  /* 准备访问下一个表元 */
    }
    printf("\n");
 }
      /* 无序链表上的动态查找 */
struct intNode *searchDSLink(struct intNode *h,int key,intNode ** pp)
{  
	struct intNode *v = h, *u = NULL;
    while (( v != NULL ) && ( v->value != key)) 
	{
        u = v;  /* 准备考察下一个表元，当前表元成为后继表元的前驱表元 */
        v = v->next; /* 考察下一个表元，后继表元成为当前表元 */
    }
    *pp = u;   return  v;
}

void createList(struct  intNode  **rpt)
{ 
	struct intNode *h, /* 链表的头指针 */
              *tail, /* 链表未尾表元的指针 */
              *p;
    int  n; char c;
    if(*rpt != NULL) 
	{
		printf("链表已存在，不允许重复创建！\n");
		return;
	}
    h = tail = NULL;   
    printf("Input data.\n");
    while (scanf("%d", &n) > 0) 
	{ /* 有整数读入 */
        p = (struct intNode *)malloc(sizeof(struct intNode));
        p->value = n;     
        p->next  = NULL;
        if (h == NULL)  h = tail = p;
	    else  tail = tail->next = p;
   }
   do  scanf("%c", &c); while(c != '\n');
   *rpt = h;
}

void  reverse (struct intNode **h)
{  
	struct intNode *p, *v1, *v2;
    v2 = *h;       /* v2 指向链表的首表元 */
    v1 = NULL;     /* 开始颠倒时，已颠倒部分为空 */
    while (v2 != NULL) 
	{ /* 还未颠倒完，循环 */
          p = v2->next;
          v2->next = v1;
          v1 = v2;
          v2 = p;
    }
    *h = v1;
}

    /* 插入新结点处理函数 */ 
void inNode(struct intNode **rpt)
{ 
	int d; struct intNode *p;
    printf("输入插入结点的值  ");  scanf("%d", &d);
    p = (struct intNode *)malloc(sizeof(struct intNode));
    p->value = d;  p->next = root;
    *rpt = p;
}
    /* 删除结点处理函数 */ 
void delNode(struct intNode **rpt)
{ int d; struct intNode *p, *q;
  printf("输入删除结点的值   ");  scanf("%d", &d);
  p = searchDSLink(root, d, &q);
  if (p == NULL) printf("没有指定值%d的结点.\n", d); 
  else 
  {
	  if(q == NULL)  *rpt = p->next;
      else 
		  q->next = p->next;
      p->next = NULL;   
	  free(p);
   }
}
     
char *menuName [] = {"创建一个整数链表", 
                      "向链表插入一个新结点",
                      "从链表删除一个结点",
                      "将链表填倒",
                      "" };
void (*fpt[])(struct intNode **) = 
     {createList, inNode, delNode, reverse, NULL};
     
void(*menu(void))(struct intNode **) /* 函数返回函数的指针 */
{   
	int ans, k;
    printf("请选择以下菜单命令。\n");
    for(k = 0; menuName[k][0] != '\0' ; k++) 
        printf("\t%d:%s\n",k+1, menuName[k]);
    printf("\t其它选择结束程序运行。\n");
    scanf("%d", &ans);
    if (ans < 1 || ans > k) 
		return NULL;
    return fpt[ans-1];/* 返回处理函数的指针 */
}
void main ()
{   
	void(*fp)(struct intNode **); 
	root = NULL;
    while (1) 
	{
		if ((fp=menu())== NULL) break;
        (*fp)(&root);
	travelLink(root);
    }
}


