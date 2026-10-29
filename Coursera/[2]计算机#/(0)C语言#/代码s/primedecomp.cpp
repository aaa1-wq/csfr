#include <stdio.h>

int main()
{
  int x;
  int i, j;
  scanf("%d", &x);

  printf("%d = ", x);

  while(x > 1)
  {
     for(i = 2; i <= x; ++i)
     {
	if(x % i == 0)
        {
           for(j = 2; j*j <= i; ++j)
             {
		if(i % j == 0) break;
             }

            if(i % j != 0 || i == 2)
            {
               x /= i;
               printf("%d", i);
               if(x != 1)
                  printf("*");
               else 
                  {
                    printf("\n");
                    break;
                  }
            }
        }
     }
  }


  return 0;

}
