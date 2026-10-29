/*	File: 生成随机数2.c
	【例5.2(p92)】产生10个0～100之间的随机数
	练习随机函数的使用和随机数的生成
	cas5.2A生成随机数.c
		增加头文件stdlib.h，并且调用库函数rand()
		运行结果总是相同的
	cas5.2B生成随机数.c
		增加头文件time.h，并且调用库函数srand()和time()，
		以获得不重复的随机数。
*/

#include <stdio.h>
#include <stdlib.h>			/* 库函数rand()和srand()所必需	*/
#include <time.h>			/* 库函数time()所必需			*/
void main()
{
	long now;
	short k, random[10];
    srand(time(&now));
	for(k=0; k<10; k++)
		random[k] = rand();
	for(k=0; k<10; k++)
		printf("%5d, %d\n", random[k], random[k]%100);
}
