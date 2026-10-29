
/* 补充题
 编写生成奇数魔方阵(2<n<MAXSIZE)的程序"。
 奇数魔方阵的定义：任何一行、一列或者两条主对角线上的元素之和均相等。
程序中用count来保存1~n的这些平方数，n为魔方阵的阶数。填完一个数后，现判是否往下移，
很简单，只要看count被n除后的余数是否为0，如果非0，说明不必下移，则需要寻找新的row,column。
主要是检查坐标是否从上方或右方越处边缘，调整行和列的脚标row,column  */


#include  <stdio.h>
#include  <stdlib.h>
#define   MAXSIZE   20

void main(void)
{
     int  matrix[MAXSIZE][MAXSIZE]; /* the magic square   */
     int  count;                    /* 1..n*n counting    */
     int  row;                      /* row index          */
     int  column;                   /* column index       */
     int  n;                       /* input n            */
     

     printf("\nOdd Number Magic Square Generator");
     printf("\n================================");
     printf("\n\n Please  input n ,2 > n < %d  --> ",MAXSIZE);
     scanf("%d",&n);
     if ( n > MAXSIZE)
          printf("\n*** ERROR ***  n should be <= %d", MAXSIZE);
     else if (n % 2 == 0) 
          printf("\n*** ERROR ***  n must be an odd integer");
     else 
	 {
          row    = 0;         /* start of from the middle */
          column = n /2;     /* of the first row.        */
          for (count = 1; count <= n*n; count++) 
		  {
               matrix[row][column] = count; /* put next # */
               if (count % n == 0)  /* move down ?    */
                    row++;    /* YES, move down one row   */
               else /* compute next indices     */
			   {         
                    row    = (row == 0) ? n - 1 : row - 1;
                    column = (column == n-1) ? 0 : column + 1;
               }
          }
          printf("\n\nMagic Square of n %d :\n\n", n);
          for (row = 0; row < n; row++) {
               for (column = 0; column < n; column++)
                    printf("%4d", matrix[row][column]);
               printf("\n");
          }
     }
	 system("pause");
}
