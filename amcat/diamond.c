#include<stdio.h>
void forward(int n){
    for (int i=0;i<=n;i++){
        for (int j=0;j<=n-i+1;j++){
            printf(" ");
        }
        for (int k=0;k<=i;k++){
            if (k==0 || k==i){
                printf("* ");
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }
}
void reverse(int n){
    for (int i=0;i<=n;i++){
        for (int j=0;j<=i+2;j++){
            printf(" ");
        }
        for (int k=0;k<=n-i;k++){
            if (k==0 || k==n-i){
                printf("* ");
            }
            else{
                printf("  ");
            }
        }
        printf("\n");
    }
}
int main(){
    int n;
    scanf("%d",&n);
    forward(n);
    reverse(n-1);
    return 0;
}