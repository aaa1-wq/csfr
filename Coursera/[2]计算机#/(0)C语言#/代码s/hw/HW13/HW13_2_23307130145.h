#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>

const char *suits[] = {"Spades", "Hearts", "Diammonds", "Clubs"};
const char *faces[] = {"Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"};

struct card{
	char a[20], b[20];
}c[53];

void initCards();
void outputCards();
void shuffle();
