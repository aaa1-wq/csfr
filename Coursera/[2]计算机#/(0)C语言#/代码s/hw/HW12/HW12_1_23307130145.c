#include<stdio.h>
int *search(int (*p)[5], int n, int id)
{
	int i;
	for (i = 0; i < n; i++)
	{
		if (**(p + i) == id)
			return *(p + i);
	}
	return 0;
}
void output(int *p)
{
	printf("%8d%8d%8d%8d%8d\n", *p, *(p + 1), *(p + 2), *(p + 3), *(p + 4));
}
int main()
{
	int list[][5] = {{201001, 75, 85, 77, 59},
	{201002, 57, 78, 73, 66}, {201003, 89, 86, 70, 90},
	{201004, 47, 70, 82, 73}, {201005, 72, 87, 88, 54},
	{201006, 90, 96, 99, 99}, {201007, 81, 97, 99, 67},
	{201008, 43, 98, 96, 79}, {201009, 67, 72, 73, 40},
	{201010, 77, 70, 82, 65}, {201011, 77, 72, 73, 80},
	{201012, 47, 70, 82, 73}, {201013, 77, 82, 83, 50},
	{201014, 97, 90, 92, 95}, {201015, 87, 92, 93, 60},
	{201016, 47, 90, 92, 73}}, i, x;
	printf("The grade form is:\n");
	for (i = 0; i < 16; i++)
		output(list[i]);
	printf("Enter a student ID: ");
	scanf("%d", &x);
	int *p = search(list, 16, x);
	if (*p != 0)
		output(p);
	else
		printf("The student ID %d is not in the grade form!");
	return 0;
}
