/* File: 指针和数组.c								*/
/* 实习目的：熟悉指针和数组的关系							*/

#include <stdio.h>
void main()
{
	int a[4]={3, 5, 7, 9}, *pa, i;
	printf("\npa = a;\tdata in array:\n");
	pa = a;
	for(i=0; i<4; i++)
	{
		printf("\ta[%d]=%d, pa[%d]=%d, ", i, a[i], i, pa[i]);
		printf("*(a+%d)=%d, *(pa+%d)=%d\n", i, *(a+i), i, *(pa+i));
	}
	printf("\npa = a;\taddress in array:\n");
	for(i=0; i<4; i++)
	{
		printf("\t&a[%d]=%X, &pa[%d]=%X, ",
			i, 0X0000FFFF & (unsigned long)&a[i],
			i, 0X0000FFFF & (unsigned long)&pa[i]);
		printf("a+%d=%X, pa+%d=%X\n",
			i, 0X0000FFFF & (unsigned long)(a+i),
			i, 0X0000FFFF & (unsigned long)(pa+i));
	}
	printf("\npa++;\tdata in array:\n");
	i = 1;
	pa++;
	printf("\ta[%d]=%d, pa[%d]=%d, ", i, a[i], 0, pa[0]);
	printf("*(a+%d)=%d, *(pa+%d)=%d\n", i, *(a+i), 0, *(pa+0));
	printf("\npa+=2;\tdata in array:\n");
	i += 2;
	pa += 2;
	printf("\ta[%d]=%d, pa[%d]=%d, ", i, a[i], 0, pa[0]);
	printf("*(a+%d)=%d, *(pa+%d)=%d\n", i, *(a+i), 0, *(pa+0));
	printf("\npa--;\tdata in array:\n");
	i--;
	pa--;
	printf("\ta[%d]=%d, pa[%d]=%d, ", i, a[i], 0, pa[0]);
	printf("*(a+%d)=%d, *(pa+%d)=%d\n", i, *(a+i), 0, *(pa+0));
}
/*

pa = a; data in array:
        a[0]=3, pa[0]=3, *(a+0)=3, *(pa+0)=3
        a[1]=5, pa[1]=5, *(a+1)=5, *(pa+1)=5
        a[2]=7, pa[2]=7, *(a+2)=7, *(pa+2)=7
        a[3]=9, pa[3]=9, *(a+3)=9, *(pa+3)=9

pa = a; address in array:
        &a[0]=FF70, &pa[0]=FF70, a+0=FF70, pa+0=FF70
        &a[1]=FF74, &pa[1]=FF74, a+1=FF74, pa+1=FF74
        &a[2]=FF78, &pa[2]=FF78, a+2=FF78, pa+2=FF78
        &a[3]=FF7C, &pa[3]=FF7C, a+3=FF7C, pa+3=FF7C

pa++;   data in array:
        a[1]=5, pa[0]=5, *(a+1)=5, *(pa+0)=5

pa+=2;  data in array:
        a[3]=9, pa[0]=9, *(a+3)=9, *(pa+0)=9

pa--;   data in array:
        a[2]=7, pa[0]=7, *(a+2)=7, *(pa+0)=7
*/
