#include <stdio.h>



void main()  
 {  
   char prog[] = "int main() {\n int a[100]; \n if(a[10]!=0) \n printf(\"OK\"); \n }";
   char *p;

	char a[100];
	int top = 0;
	int unmatch = 0;
	a[top] = 0;
	int i = 0;

	for(p = prog; *p; ++p, ++i)
	{
		if(*p == '(' || *p == '['|| *p == '{')
		{
			top++;
			a[top] = *p;
		}
		else if(*p == ')')
		{
			if(a[top] != '(')
			{
				unmatch = 1;
				break;
			}
			else
				top--;
			
		}
		else if(*p == ']')
		{
			if(a[top] != '[')

			{
				unmatch = 1;
				break;
			}
			else
				top--;

		}
		else if(*p == '}')
		{
			if(a[top] != '{')
			{
				unmatch = 1;
				break;
			}
			else
				top--;

		}
	}

	if(unmatch || top != 0) printf("not match\n");
	else printf("match\n");

 }  