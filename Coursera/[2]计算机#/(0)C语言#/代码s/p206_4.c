#include <stdio.h>
#include <stdlib.h>
void write(FILE *f)
{
	int i=0,x;
	printf("\nOUTPUT SORT/MERGER FILE OF INTEGER :\n\n");
	while(fscanf(f,"%d\n",&x)==1)
		printf("%d%c",x,++i%5?'\t':'\n');
	fclose(f);
}

void connect(FILE *f[])	//f[2]文件为f[0],f[1]文件按大小的合并（除去重复）
{	
	int n,//存放输入文件1的数据
		m,//存放输入文件0的数据
		x,//存放n,m中小的数据
		conmerge;//文件结束符的标志
	conmerge=!(feof(f[0])&&feof(f[1]));
	fscanf(f[0],"%d",&m);
	fscanf(f[1],"%d",&n);
	while(conmerge)	 
	{ 
		if(m>n)
		{
			x=n;
			fscanf(f[1],"%d",&n);//取输入文件1的下一个读数据给n
			conmerge=!(feof(f[1]));
		}
		else if(m==n)//除去重复
		{
			x=n;//重复数据只给其中的一个
			fscanf(f[0],"%d",&m);//取下一个
			fscanf(f[1],"%d",&n);//取下一个
			conmerge=!(feof(f[0])||feof(f[1]));
		}
	    else
		{
			x=m;
			fscanf(f[0],"%d",&m);//取输入文件0的下一个读数据给m
			conmerge=!(feof(f[0]));
		}
		fprintf(f[2],"%d\n",x);//将x给输出文件
	}
	while(!feof(f[0]))//从输入文件0向输出文件写数据
	{
		fprintf(f[2],"%d\n",m);
		fscanf(f[0],"%d",&m);
	}
    while(!feof(f[1]))//从输入文件1向输出文件写数据
	{
		fprintf(f[2],"%d\n",n);
		fscanf(f[1],"%d",&n);
	}
    fclose(f[0]);
    fclose(f[1]);
}

void main()
{ 
    FILE *f[3];
	char fname[2][20];
	int i;
	for(i=0;i<2;i++)
	{
		printf("Enter file%d name:\n",i+1);
	    gets(fname[i]);//输入文件名
	    if ((f[i]=fopen(fname[i],"r"))==NULL)
		{
	       printf("cannot open file1 \n");
		   exit(0);
		}
    }
    if((f[i]=fopen("outfile.txt","w+"))==NULL)
	
	{
		printf("cannot open file3 \n");
		exit(0);
	}
    connect(f);//合并
	f[2]=fopen(fname[1],"r");
	write(f[2]);
}