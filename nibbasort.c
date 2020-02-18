#include<stdio.h>
int findmin(int arr[], int n)
{
    int min = 6000;
    int res = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
            res = i;
        }
    }
    return res;
}
int main()
{
    int size;
    printf("enter size of the array u nibba:");
    scanf("%d",&size);
    int arr[20];
    for (int i=0;i<size;i++)
    {
        scanf("%d",&arr[i]);
    }
    int sortedarray[20];
    int j=0;
    for(int i=0;i<size;i++)
    {
        int x=findmin(arr,size);
        sortedarray[j]=arr[x];
        arr[x]=66000;
        j+=1;

    }
    for(int j=0;j<size;j++)
    {
        printf("%d\t",sortedarray[j]);
    }
    printf("\n");


    return 0;
}
