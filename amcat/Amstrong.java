import java.util.*;
class Amstrong{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int c=n;
        int summ=0,rem=0;
        while (n>0){
            rem=n%10;
            summ+=(rem*rem*rem);
            n=(int)n/10;
        }
        if (summ==c){
        System.out.println("Amstrong");
        }
        else{
            System.out.println("Not Amstrong");
        }
    }
}