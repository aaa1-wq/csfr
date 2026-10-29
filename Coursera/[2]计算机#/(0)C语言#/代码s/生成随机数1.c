/*	File: 生成随机数.c
	【例5.2(p92)】产生10个0～100之间的随机数
	练习随机函数的使用和随机数的生成
		增加头文件stdlib.h，并且调用库函数rand()
		运行结果总是相同的						*/

#include <stdio.h>
#include <stdlib.h>
void main()
{
	short k, random[10];
	for(k=0; k<10; k++)
		random[k] = rand();
	for(k=0; k<10; k++)
		printf("%5d, %d\n", random[k], random[k]%100);
}
/*
   41, 41
18467, 67
 6334, 34
26500, 0
19169, 69
15724, 24
11478, 78
29358, 58
26962, 62
24464, 64
*/