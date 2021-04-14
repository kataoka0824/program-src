#include<stdio.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<unistd.h>
#include<pthread.h>
#include<string.h>
void recv_thread(void);
int sock;
int main(void){
    pthread_t t1;
    struct sockaddr_in addr;
    char send_buf[2048];
    sock=socket(AF_INET,SOCK_DGRAM,0);
    addr.sin_family=AF_INET;
    addr.sin_port=htons(atoi[1]);
    addr.sin_addr.s_addr=INADDR_ANY;
    bind(sock,(struct sockaddr*)&addr,sizeof(addr));
    pthread_create(&t1,NULL,(void*)recv_thread,(void*)NULL);
    addr.sin_port=htons(atoi[2])
}