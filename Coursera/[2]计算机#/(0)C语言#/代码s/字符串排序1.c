/*	File:×Ö·û´®ÅÅÐò1.c
	¡¾Àý4-25¡¿×Ö·û´®ÅÅÐò·½°¸Ò»	*/

#include <stdio.h>
#include <stdlib.h>
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
void bubble3(char *w[], short n)
{
	short i, j;
	for(i=n-1; i>0; i--)
	for(j=0; j<i; j++)
		if(*w[j] > *w[j+1])
			swap3(w, j, (short)(j+1));
}
void main()
{
	short j, n=7;
	printf("Before sorting\n");
	for(j=0; j<n; j++)
		printf("\t%s\n", weekday[j]);
	bubble3(weekday, n);
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
        Sunday
        Saturday
        Tuesday
        Thursday
        Wednesday
*/
