#include<stdio.h>
#include<unistd.h>
#include<pthread.h>

void func(int x);

int main(void){
    pthread_t t1;
    pthread_t t2;
    printf("main()\n");
    pthread_create(&t1,NULL,(void*)func,(void*)1);
    pthread_create(&t2,NULL,(void*)func,(void*)2);
    pthread_join(t1,NULL);
    pthread_join(t2,NULL);
    return 0;
}

void func(int x){
    int i;
    if(x==1){
        for(i=0;i<10;i++){
            printf("func(%d):%d\n",x,i);
            usleep(100000);
        }
    }
    if(x==2){
        for(i=0;i<10;i++){
            printf("func(%d):%d\n",x,i);
            usleep(200000);
        }
    }
}