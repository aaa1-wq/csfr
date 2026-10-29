#include<stdio.h>
int main(){
	int a,n;
	float sum=0;
	a=0;
	n=0;
	scanf("%d",&a);
	
	while (a!=-1) {
		if(a<=100&&a>=0){
			sum=sum+a;
			n=n+1;
		}
		scanf("%d",&a);	
    }	
    printf("%.2f",sum/n);
    return 0 ;
}

