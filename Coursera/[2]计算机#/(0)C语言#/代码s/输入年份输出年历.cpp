#include<cstdlib>
#include<cstdio>
using namespace std;
const int D[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int main()
{
    int Year;
    bool R;
    scanf("%d",&Year);
    if ((Year%100!=0&&Year%4==0)||Year%400==0) R=true; else R=false;
    for (int i=1;i<=12;i++)
    {
        printf("%d:\n",i);
        for (int j=0;j<=6;j++) printf("%3d",j);
        printf("\n");
        int f;
        if (i<3) f=Year-1; else f=Year;
        int g;
        if (i<3) g=i+13; else g=i+1;
        int N=1461*f/4+153*g/5+1;
        int d=(N-621049)%7;
        for (int j=0;j<d;j++) printf("   ");
        printf("  1");
        for (int j=2;j<=D[i]+(i==2&&R);j++)
        {
            d++;
            if (d==7)
            {
                     d=0;
                     printf("\n");
            }
            printf("%3d",j);
        }
        printf("\n");
    }
    system("pause");
    return 0;
}
