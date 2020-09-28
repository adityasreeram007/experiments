import java.util.*;
class Automorphic{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if (n%10==(n*n)%10){
            System.out.println("automorphic");
        }
        else{
            System.out.println("not automorphic");
        }
        
    }
}