#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 定义链表节点结构体
typedef struct Node {
    char data;
    struct Node* next;
} Node;

// 创建环形链表
Node* makeLoop(const char* text) {
    Node* head = NULL;
    Node* tail = NULL;
    int length = strlen(text), i;
    for (i = 0; i < length; i++) {
        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->data = text[i];
        if (head == NULL) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
    }
    if (tail != NULL) {
        tail->next = head;  // 尾节点指向头节点形成环
    }
    return head;
}

// 加密/解密函数
void process(const char* text, int key, int decrypt) {
    Node* head = makeLoop(text);
    Node* current = head;
    int length = strlen(text), i;
    printf("Result: ");
    for (i = 0; i < length; i++) {
        int steps = key % length, j;
        if (decrypt) {
            steps = length - steps;  // 解密时相当于逆向移动
        }
        for (j = 0; j < steps; j++) {
            current = current->next;
        }
        printf("%c", current->data);
    }
    printf("\n");
}

int main() {
    char text[] = "abcde";
    int key = 3;
    
    printf("Original: %s\n", text);
    
    // 加密
    process(text, key, 0);
    
    // 解密
    process("caebd", key, 1);

    return 0;
}
