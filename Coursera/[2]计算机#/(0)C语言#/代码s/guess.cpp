#include <stdlib.h>
#include <stdio.h>
#include <time.h>


void main()
{
   int i, j;
   int k;
   int a[4];
   int b[4];
   int cnt_a, cnt_b;
   int error;

   // generate four different random numbers
   srand(time(0));
   for(i = 0; i < 4; ++i)
   {
      while(1)
      {
          a[i] = rand() % 8 + 1;
          for(j = 0; j < i; ++j)
            {
               if(a[i] == a[j])
                 break;
            }
          if(j == i) break;
      }
   }

   // try eight times
   for(k = 0; k < 8; ++k)
   {
      // get inputs
      for(i = 0; i < 4; ++i)
       scanf("%d", &b[i]);
      
      // check the validation of the inputs
      error = 0;
      for(i = 0; i < 4; i++)
        for(j = 0; j < 4; ++j)
             if((i != j && b[i] == b[j]) || b[i] > 8 || b[i] < 1)
               {
                  error = 1;
	          break;
               }
      if(error)
      {
         printf("input error\n");
         continue;
      }

    // check counter A and counter B
    cnt_a = 0; cnt_b = 0;
    for(i = 0; i < 4; ++i)
     {
        for(j = 0; j < 4; ++j)
         {
             if(a[i] == b[j])
             {
                 if(i == j)
                    cnt_a++;
                 else
                    cnt_b++;
             }
         }
     }
    printf("%dA%dB\n", cnt_a, cnt_b);

    // guess right, break
    if(cnt_a == 4) break;

   }


}