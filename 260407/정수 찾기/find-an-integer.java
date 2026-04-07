import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        HashSet<Integer> A = new HashSet<>();
        while(N -- > 0){
            A.add(sc.nextInt());
        }

        int M = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        while(M -- > 0){
            int num = sc.nextInt();
            if(A.contains(num))sb.append("1").append("\n");
            else sb.append("0").append("\n");

        }

        System.out.println(sb);
    }
}