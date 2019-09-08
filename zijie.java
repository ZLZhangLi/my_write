import java.util.*;
import java.io.*;
import java.lang.reflect.Array;
public class Main {
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N = sc.nextInt();
        N=N/2;
        long[]data=new long[N+1];
        data[0]=1;
        data[1]=1;
        for (int i=2;i<=N;i++){
            for (int j=1;i<=i;j++){
                data[i]+=(data[j-1]*data[i-j]);
                data[i]=data[i]%1000000007;
            }
        }
        System.out.println(data[N]);
    }