/*	File: ×Ö·û´®ÅÅÐò2.c
	×Ö·û´®ÅÅÐò·½°¸¶þ	*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char	w0[] = "Sunday",
		w1[] = "Monday",
		w2[] = "Tuesday",
		w3[] = "Wednesday",
		w4[] = "Thursday",
		w5[] = "Friday",
		w6[] = "Saturday";
char *weekday[] = {w0, w1, w2, w3, w4, w5, w6};
void swap3(char *w[], short w1, short w2)
{
	char *t;
	t = w[w1];
	w[w1] = w[w2];
	w[w2] = t;
}
void bubble4(char *w[], short n)
{
	short i, j;
	for(i=n-1; i>0; i--)
		for(j=0; j<i; j++)
			if(strcmp(w[j], w[j+1]) > 0)
				swap3(w, j, (short)(j+1));
}
void main()
{
	short j, n=7;
	printf("Before sorting\n");
	for(j=0; j<n; j++)
		printf("\t%s\n", weekday[j]);
	bubble4(weekday, n);
	printf("After sorting\n");
	for(j=0; j<n; j++)
		printf("\t%s\n", weekday[j]);
}
/*
Before sorting
        Sunday
        Monday
        Tuesday
        Wednesday
        Thursday
        Friday
        Saturday
After sorting
        Friday
        Monday
        Saturday
        Sunday
        Thursday
        Tuesday
        Wednesday
*/
