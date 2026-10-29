/*	File: 删去字符1.c
	【例4-20】在已知的字符串中删去某个字符
	rmcharA()	采用下标法编程
*/

#include <stdio.h>
char *rmcharA(char s[], char c)
{
	int i=0,j=0; 
	char *q=s;
	while(s[i])
	{
		if(s[i] != c)
			q[j++] = s[i];
 	    i++;
	}
	q[j] = '\0';
	printf("q=%s\n",q);
	return(q);
}
void main()
{
	char s[80], c, *q;
	printf("source string: ");
	gets(s);
	printf("char to be removed: ");
	scanf("%c", &c);
	q = rmcharA(s, c);
	printf("removed string by rmcharA: [%s]\n", q);
}
/*
source string: 12345
char to be removed: 3
q=1245
removed string by rmcharA: [1245]


source string: ASDFG
char to be removed: K
q=ASDFG
removed string by rmcharA: [ASDFG]

*/
