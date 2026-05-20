import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        TreeSet<int[]> ts = new TreeSet<>((a, b) -> {
            if(a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });

        for(int i = 0 ; i < N ; i ++){
            int x = sc.nextInt();
            int y = sc.nextInt();

            ts.add(new int[]{x, y});
        }
        StringBuilder sb = new StringBuilder();

        for(int i = 0 ; i < M ; i ++){
            int n = sc.nextInt();

            int[] find = ts.ceiling(new int[]{n, 0});

            if(find == null){
                sb.append("-1 -1\n");
            }else{
                sb.append(find[0] + " " + find[1]).append("\n"); 
                ts.remove(find);
            }

        }

        System.out.println(sb);
    }
}