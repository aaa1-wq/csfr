//26303056007
#include<stdio.h>
#include <math.h>
int main(){
//	double a,k;
//	scanf("%lf",&a);
//	k = (a < 0) ? -a : a;
//	printf("%.3f",k);
//	return 0;
	double x1,x2,y1,y2,dist;
	scanf("%lf %lf %lf %lf",&x1,&x2,&y1,&y2);
	dist = sqrt(pow(x1 - y1, 2) + pow(x2 - y2, 2));
	printf("%.3f",dist);
	return 0;
	
}
