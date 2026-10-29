#include <stdio.h>
#include <string.h>
void main()
{ 
	FILE *f1,*f2;
	int  i,j=0;
	char fname1[50],fname2[50],a[101],c;
	printf("请输入源文件名:\n");
	scanf("%s%*c",fname1);
	if ((f1=fopen(fname1,"r"))==NULL)
	{ 
		printf("cannot open file1 \n");
		return ;
	}
	printf("请输入目标文件名:\n");
	scanf("%s%*c",fname2);
	if ((f2=fopen(fname2,"w+"))==NULL)
	{ 
		printf("cannot open file2 \n");
		return ;
	}
	printf("请输入目标文件每行的字符数:\n注意：每行字符数<=100.\n");
	printf("0----按原样复制:\nx数字---每行按x个字符复制，例如输入50，则每行为50个字符\n");
	scanf("%d",&i);
	do
	{
		if(i==0)
		{
			fgets(a,100,f1);
			fputs(a,f2);		
		}
		else 
		{
			c=fgetc(f1);
			if(c!='\n')
			{
				j++;
				fputc(c,f2);
			}
			if(j==i)
			{
				fputc('\n',f2);
				j=0;
			}
		}
	}while(!feof(f1));
	fclose(f1);
	fclose(f2);
}


