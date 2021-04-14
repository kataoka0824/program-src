#include<stdio.h>
int tasu(int a, int b){
    int c;
    c=a+b;
    return c;
}
int main(void){
    int x,y,z;
    printf("x=");
    scanf("%d",&x);
    printf("y=");
    scanf("%d",&y);
    z=tasu(x,y);
    printf("z=%d\n",z);
    return 0;
}
