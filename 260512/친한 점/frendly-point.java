import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        TreeSet<int[]> ts = new TreeSet<>((a,b) -> {
            if(a[0] == b[0]){
                return Integer.compare(a[1], b[1]);
            }else{
                return Integer.compare(a[0], b[0]);
            }
        });

        for(int i = 0 ; i < N ; i ++){
            ts.add(new int[]{sc.nextInt(), sc.nextInt()});
        }

        StringBuilder sb  = new StringBuilder();

        for(int i = 0 ; i < M ; i ++){
            int[] c = ts.ceiling(new int[]{sc.nextInt(), sc.nextInt()});
            if(c == null){
                sb.append(-1 + " " + -1).append("\n");
            }else{
                sb.append(c[0] + " " + c[1]).append("\n");
            }
        }

        System.out.println(sb);


    }
}