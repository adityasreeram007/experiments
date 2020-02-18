#include<stdio.h>
#include<string.h>
int main()
{

    char str[14];
    char search[4];
    scanf("%s",str);
    scanf("%s",search);
    int c=strlen(search);
    //printf("%d",c);
    int i=0,j;
    int flag=0;
    for (i=0;i<strlen(str)-c;i++)
    {   flag=0;
        for (j=0;j<c;j++)
        {
            if(str[i+j]==search[j])
            {
                flag=1;
            }
            else{
                flag=0;
                break;
            }
        }
        if(flag==1)
        {
            printf("%d",i);
            break;
        }

    }
    return 0;
}