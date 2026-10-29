#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int main()
{
	srand(time(NULL));
	int n, *p, i, c1, c2, c3, c4, c5;
	c1 = c2 = c3 = c4 = c5 = 0;
	printf("Enter the number of the students: ");
	scanf("%d", &n);
	p = (int *)malloc(n * sizeof(int));
	printf("Randomly generate the grades of %d students:\n");
	for (i = 0; i < n; i++)
	{
		p[i] = rand() % 101;
		printf("%d ", p[i]);
		if (p[i] >= 0 && p[i] < 60)
			c1++;
		else if (p[i] >= 60 && p[i] < 70)
			c2++;
		else if (p[i] >= 70 && p[i] < 80)
			c3++;
		else if (p[i] >= 80 && p[i] < 90)
			c4++;
		else
			c5++;
	}
	printf("\nThe statistics of each score segment:\n");
	printf("[0,60): %d人\n", c1);
	printf("[60,70): %d人\n", c2);
	printf("[70,80): %d人\n", c3);
	printf("[80,90): %d人\n", c4);
	printf("[90,100]: %d人\n", c5);
	return 0;
}
