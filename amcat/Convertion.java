import java.util.*;
import java.lang.*;
class Convertion{
    static int bintoint(String str){
        int sumx=0;
        for(int i=str.length()-1;i>=0;i--){
            if (str.charAt(i)=='1'){
                sumx+=Math.pow(2,str.length()-i-1);
            }
        }
        return sumx;

    }
    static int bintointauto(String str){
        return Integer.parseInt(str,2);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String n=sc.next();
        System.out.println(bintointauto(n));

        
    }
}