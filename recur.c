#include<stdio.h>
#include<string.h>
char temp[10];
int i=0;
#define CLEAR(temp) memset(temp,'\0',10)
void printrever(char str[], int x)
{
    if(x==-1){
        return ;
    }
    if(str[x]==' '){
        printf("%s",strrev(temp));
        CLEAR(temp);
        i=0;
        
    }
    temp[i]=str[x];

    i+=1;
    printrever(str, x - 1);
}
int main()
{
    char str[100];
    char c;
    scanf("%c",&c);
    int i=0;
    str[i]=c;
    while(c!='\n')
    {
        str[i]=c;
        scanf("%c",&c);
        i+=1;
    }
    printf("%s",str);
    printrever(str,strlen(str)-1);
    return 0;
}
