#define N 3
#include <stdio.h>
//  (1)   根据题意是沿着对角线将a[i][j]交换成a[j][i]
void main()
{ 
	int a[N][N],i,j,k=1,t,*p=&a[0][0]; //p=a[0]；
	while(k<=N*N)
	    *p++=k++;
    p=a[0];   //将指针调整到首地址
	for(i=0;i<N;i++)
		for(j=i;j<N;j++)
		{
			t=*(p+i*N+j);
			*(p+i*N+j)=*(p+j*N+i);
			*(p+j*N+i)=t;
		}
//输出a[i][j]
	for(i=0;i<N*N;i++)
	{
		if(i%N==0)printf("\n");
		printf("%4d",*p++);	
	}
	printf("\n");
	/*for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
			printf("%4d",*(p+i*N+j));
	    printf("\n");
	}*/
}