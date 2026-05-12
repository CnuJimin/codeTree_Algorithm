import java.util.*;

public class Main {
    public static void main(String[] args) {
        TreeSet<Integer> ts = new TreeSet<>();

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        for(int i = 0 ; i < N ; i ++){
            ts.add(sc.nextInt());
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 0 ; i < M ; i ++){
            Integer num = ts.ceiling(sc.nextInt());
            if(num == null){
                sb.append(-1).append("\n");
            }else{
                sb.append(num).append("\n");
            }
        }

        System.out.println(sb);
    }
}