#include<stdio.h>
#include<string.h>
int main()
{
    char str[]="millionaireunderconstruction";
    
    int m=strlen(str);
    char table[m][m];
    int i=0;
    int j=m-1;
    while(i<m)
    {
        table[i][i]=str[i];
        i+=1;
    }
    i=0;
    while(j>=0 && i<=m)
    {
        table[j][i]=str[i];
        j-=1;
        i+=1;
    }
    for(i=0;i<m;i++)
    {
        for (j=0;j<m;j++)
        {
            if(i==j || i+j==m-1){
                printf("%c ",table[i][j]);
            }
            else{
                printf(" ");
            }
            
        }
        printf("\n");
    }
}