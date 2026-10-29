/* File:数组指针运算示例	*/
#include <stdio.h>
void main()
{
	unsigned long SIZE = sizeof(unsigned long);
	long q[5] = {1, 2, 5, 7, 10}, *pq;
	pq = q;
	/* 假设q的首地址为F100					*/

	/* 元素值运算，得：10 + 4 = 14			*/
	printf("(1) q[4] + 4 = %d + 4 = %d\n\n", q[4], q[4]+4);

	/* 元素值运算，得：7 - 2 = 5			*/
	printf("(2) pq[3] - 2 = %d - 2 = %d\n\n", pq[3], pq[3]-2);

	/* 元素值运算，得：10 - 2 = 8			*/
	printf("(3) *(pq + 4) - *(q + 1) = %d - %d = %d\n\n",
		*(pq + 4), *(q + 1), *(pq + 4) - *(q + 1));
	
	/* 地址运算，得：F100 + 4 * 4 = F110	*/
	printf("(4) q + 4 = %X + 4 = %X\n", q, q + 4);
	printf("(4) 地址运算：F100 + 4 * 4Byte = F110\n");
	printf("(4) 地址运算：%X + 4 * 4Byte = %X\n\n", 
		(unsigned long)q & 0X0000FFFF,
		((unsigned long)q + 4UL * SIZE) & 0X0000FFFF);
	
	/* 地址运算，得：F10C - 2 * 4 = F104	*/
	printf("(5) &q[3] - 2 = %X - 2 = %X\n", &q[3], &q[3] - 2);
	printf("(5) 地址运算：F10C - 2 * 4Byte = F104\n");
	printf("(5) 地址运算：%X - 2 * 4Byte = %X\n\n",
		(unsigned long)(&q[3]) & 0X00FFFF,	
		((unsigned long)(&q[3]) - 2UL * SIZE) & 0X00FFFF);
	
	/* 地址和元素值混合运算，得：F100 + 4 * 4 - 2 * 4 = F108	*/
	printf("(6) pq + 4 - *(q + 1) = %X + 4 - %d = %X\n",
		pq, *(q + 1), pq + 4 - *(q + 1));
	printf("(6) 地址运算：F100 + 4 * 4Byte - 2 * 4Byte = F108\n");
	printf("(6) 地址运算：%X + 4 * 4Byte - 2 * 4Byte = %X\n\n",
		(unsigned long)pq & 0X00FFFF,	
		((unsigned long)pq + 4UL * SIZE - *(q + 1) * SIZE) & 0X00FFFF);
	
	/* 地址和元素值混合运算，得：F100 + 1 * 4 + 1 * 4 = F108	*/
	printf("(7) pq + *q + 1 = %X + %d + 1 = %X\n",
		pq, *q, pq + *q + 1);
	printf("(7) 混合运算：F100 + 1 * 4Byte + 1 * 4Byte = F108\n");
	printf("(7) 混合运算：%X + 1 * 4Byte + 1 * 4Byte = %X\n\n",
		(unsigned long)pq & 0X00FFFF,	
		((unsigned long)pq + 1UL * SIZE + 1UL * SIZE) & 0X00FFFF);
	
	/* 数值类型的地址运算					*/
	printf("(8) (pq + 4) - (q + 1) = %X - %X = %d\n",
		(pq + 4), (q + 1), (pq + 4) - (q + 1));
	printf("(8) 数值地址运算：\n");
	printf("    ((F100 + 4 * 4Byte) - (F110 + 1 * 4Byte)) / 4Byte\n");
	printf("    = (F110 - F104) / 4Byte = 3\n");
	printf("(8) 数值地址运算：\n");
	printf("    ((%X + 4 * 4Byte) - (%X + 1 * 4Byte)) / 4Byte\n",
		(unsigned long)pq & 0X00FFFF, (unsigned long)q & 0X00FFFF);
	printf("    = (%X - %X) / 4Byte = %d\n\n",
		((unsigned long)pq + 4 * SIZE) & 0X00FFFF, 
		((unsigned long)q  + 1 * SIZE) & 0X00FFFF,	
		( ((unsigned long)pq + 4 * SIZE) -
		  ((unsigned long)q  + 1 * SIZE) ) / SIZE);
}
/*
(1) q[4] + 4 = 10 + 4 = 14

(2) pq[3] - 2 = 7 - 2 = 5

(3) *(pq + 4) - *(q + 1) = 10 - 2 = 8

(4) q + 4 = 13FF68 + 4 = 13FF78
(4) 地址运算：F100 + 4 * 4Byte = F110
(4) 地址运算：FF68 + 4 * 4Byte = FF78

(5) &q[3] - 2 = 13FF74 - 2 = 13FF6C
(5) 地址运算：F10C - 2 * 4Byte = F104
(5) 地址运算：FF74 - 2 * 4Byte = FF6C

(6) pq + 4 - *(q + 1) = 13FF68 + 4 - 2 = 13FF70
(6) 地址运算：F100 + 4 * 4Byte - 2 * 4Byte = F108
(6) 地址运算：FF68 + 4 * 4Byte - 2 * 4Byte = FF70

(7) pq + *q + 1 = 13FF68 + 1 + 1 = 13FF70
(7) 混合运算：F100 + 1 * 4Byte + 1 * 4Byte = F108
(7) 混合运算：FF68 + 1 * 4Byte + 1 * 4Byte = FF70

(8) (pq + 4) - (q + 1) = 13FF78 - 13FF6C = 3
(8) 数值地址运算：
    ((F100 + 4 * 4Byte) - (F110 + 1 * 4Byte)) / 4Byte
    = (F110 - F104) / 4Byte = 3
(8) 数值地址运算：
    ((FF68 + 4 * 4Byte) - (FF68 + 1 * 4Byte)) / 4Byte
    = (FF78 - FF6C) / 4Byte = 3

*/
