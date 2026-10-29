#include <stdio.h>

int main(void) {
    double a,b;
    char c;
    int n;
    float sto[100];
    scanf("%d",&n);
    for (int i = 0; i < n; i++) {
    	scanf("%lf %c %lf",&a,&c,&b);
    	switch(c){
	    	case('+'):
	    		sto[i]=("%.2f",a+b);break;
	     	case('-'):
	    		sto[i]=("%.2f",a-b);break;
	     	case('*'):
	    		sto[i]=("%.2f",a*b);break;
	     	case('/'):
	    		sto[i]=("%.2f",a/b);break;
		}   
    }
    for (int i = 0; i < n; i++){
    	printf("%.2f\n",sto[i]);
	}
    return 0;
}
