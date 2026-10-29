#include"HW13_2_23307130145.h"

int main()
{
	int i;
	srand(time(NULL));
	initCards();
	printf("\t\t\t/* Shuffling Cards Program */\n");
	printf("The initial cards are:\n");
	outputCards();
	shuffle();
	printf("The shuffled cards are:\n");
	outputCards();
	return 0;
}
void initCards()
{
	int i, j, num = 0; 
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 13; j++)
		{
			strcpy(c[num].a, suits[i]);
			strcpy(c[num].b, faces[j]);
			num++;
		}
	}
}
void outputCards()
{
	int i, j, num = 0;
	for (i = 0; i < 8; i++)
	{
		for (j = 0; j < 6; j++, num++)
			printf("%-11s%-6s|", c[num].a, c[num].b);
		printf("\n");
	}
	for (i = 0; i < 4; i++, num++)
		printf("%-11s%-6s|", c[num].a, c[num].b);
	printf("\n\n");
}
void shuffle()
{
	int x, i;
	for (i = 0; i < 52; i++)
	{
		x = rand() % 52;
		struct card temp = c[x];
		c[x] = c[i];
		c[i] = temp;
	}
}
