#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1000
#define ENCRYPT 1  //标志常量, 代表加密 
#define DECRYPT 2  //标志常量, 代表解密 

//环形链表的表元类型 
struct node
{
	int i;
	struct node *next;
};
typedef struct node Node; 
Node *makeLoop(const char *text)
{
    Node *head = NULL;
    Node *tail = NULL;
    int length = strlen(text), j;
    for (j = 0; j < length; j++)
	{
        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->i = j;
        if (head == NULL)
		{
            head = newNode;
            tail = newNode;
        }
		else
		{
            tail->next = newNode;
            tail = newNode;
        }
    }
    if (tail != NULL)
        tail->next = head;  // 尾节点指向头节点形成环
    return tail;
}
void process(const char* text, int key, char* t, int decrypt)
{
	Node* tail = makeLoop(text);
    Node* head = tail->next;
    Node* s = head, *sf = tail;
    int length = strlen(text), j;
    for (j = 0; j < length; j++)
	{
        int steps = key % length, k;
        for (k = 0; k < steps - 1; k++)
        {
        	sf = s;
            s = s->next;
		}
        if (decrypt == 1)
        	t[j] = text[s->i];
        else
        	t[s->i] = text[j];
        sf->next = s->next;
        free(s);
        s = sf->next;
    }
    t[j] = '\0';
}
int main()
{
	int key;
	char original[N], cipher[N], decipher[N];

	printf("Enter some text (length < %d):\n", N);
	gets(original);
	printf("Enter the key: ");
	scanf("%d", &key);

	process(original, key, cipher, ENCRYPT);  //加密 
	printf("The cipher:\n%s\n", cipher);
	process(cipher, key, decipher, DECRYPT);  // 解密 
	printf("The decipher:\n%s\n", decipher);

	return 0;
}
