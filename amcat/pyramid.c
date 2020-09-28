#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        int j=0;
        for (int x=0;x<n-i+3;x++){
            printf("*");
        }
        for (j=1;j<=i;j++){
            printf("%d*",j);
        }
        for (int k=j-2;k>=1;k--){
            printf("%d*",k);
        }
        printf("\n");
    }
    return 0;
}