#include<stdio.h>
#define MAX  100

int order(int m[],int n)//删去数组m中的重复元素，并按从小到大排序
{
	int i,j,k;
	printf("数组M中含有的元素个数为:%d\n",n);
	for(i=1;i<n;i++)//按冒泡法排序
	{
		for(j=i;j>0;j--)
		{
			while(m[j]==m[j-1])//删除重复元素
			{
				for(k=j;k<n-1;k++)
				{
					m[k]=m[k+1];
					printf("出现重复元素\n");
				}
				n--;
			}
			if(m[j]<m[j-1])
			{
				int t=m[j];
				m[j]=m[j-1];
				m[j-1]=t;
				printf("出现元素交换\n");
			}
		}
	}
	printf("完成后的n的值为：%d\n",n);
	return n;
}

void main()
{
	int a[MAX],n,i=0;
	printf("请输入要输入数组元素的个数N\n");
	scanf("%d",&n);
	printf("请依次输入数组的元素\n");
	while(i<n)
	{
		scanf("%d",&a[i]);
		i++;
	}
	printf("数组输入完毕\n");
	n=order(a,n);
	printf("删除重复元素并排序后的结果为：\n");
	for(i=0;i<n;i++)
		printf("%d\t",a[i]);
	printf("\n");
}