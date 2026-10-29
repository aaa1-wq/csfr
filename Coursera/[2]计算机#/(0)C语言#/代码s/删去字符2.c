/*	File: 删去字符2.c
	在已知的字符串中删去某个字符
	rmcharB()	采用指针法编程
*/

#include <stdio.h>
char *rmchar(char *s, char c)
{
	int i=0; 
	char *p=s, *q=s;
	while(*s)
	{
		if(*s != c)
			*p++ = *s;
		s++;
	}
	*p = '\0';
    return(q);
}
void main()
{
	char s[80], c, *q;
	printf("source string: ");
	gets(s);
	printf("char to be removed: ");
	scanf("%c", &c);
	q = rmchar(s, c);
	printf("removed string by rmchar: [%s]\n", q);
}
/*
source string: 12345
char to be removed: 3
removed string by rmchar: [1245]

source string: 12345
char to be removed: 7
removed string by rmchar: [12345]
*/
