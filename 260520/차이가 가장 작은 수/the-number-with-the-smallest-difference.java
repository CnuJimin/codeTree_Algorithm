import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        TreeSet<Integer> ts = new TreeSet<>();

        for(int i = 0 ; i < N ; i ++){
            ts.add(sc.nextInt());
        }

        int ans = Integer.MAX_VALUE;

        for(Integer n : ts){
            Integer bigger = ts.ceiling(n + M);
            if(bigger != null){
                ans = Math.min(ans, Math.abs(bigger - n));
            }
        }

        if(ans == Integer.MAX_VALUE) ans = -1;

        System.out.println(ans);

    }
}