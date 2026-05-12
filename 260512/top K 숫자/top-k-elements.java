import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        TreeSet<Integer> ts = new TreeSet<>();
        for(int i = 0 ; i < N ; i ++){
            ts.add(sc.nextInt());
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0 ; i < K ; i ++){
            sb.append(ts.last() + " ");
            ts.remove(ts.last());
        }

        System.out.println(sb);

    }
}