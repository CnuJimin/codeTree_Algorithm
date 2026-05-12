import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        TreeSet<Integer> ts = new TreeSet<>();

        for(int i = 1 ; i <= M ; i ++){
            ts.add(i);
        }

        for(int i = 0 ; i < N ; i ++){
            int num = sc.nextInt();

            ts.remove(num);

            System.out.println(ts.last());
        }
    }
}