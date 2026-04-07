import java.util.*;

public class Main {

    static class Node{
        int v;
        public Node(int v){
            this.v = v;
        }
    }

    static class Pair{
        int x, y;

        public Pair(int x, int y){
            this.x = x; 
            this.y = y;
        }
    }

    public static void main(String[] args) {
        // Please write your code here.
        // 총 3번 반복 
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        HashSet<Integer>[] hashArr = new HashSet[N + 1];

        for(int i = 0 ; i <= N ; i ++){
            hashArr[i] = new HashSet<>();
            hashArr[i].add(i);
        }

        Node[] seats = new Node[N + 1];

        for(int i = 1 ; i <= N ; i ++){
            seats[i] = new Node(i);
        }

        Pair[] changes = new Pair[K];

        for (int i = 0 ; i < K ; i ++){
            changes[i] = new Pair(sc.nextInt(), sc.nextInt());
        }

        for(int i = 0 ; i < 3 * K ; i ++){
            int idx = i % K;
            Pair change = changes[idx];

            Node a = seats[change.x];
            Node b = seats[change.y];

            hashArr[a.v].add(change.y);
            hashArr[b.v].add(change.x);

            Node temp = a;
            seats[change.x] = b;
            seats[change.y] = temp;
        }

        StringBuilder sb = new StringBuilder();

        for(int i = 1; i <= N ; i ++){
            sb.append(hashArr[i].size()).append("\n");
        }

        System.out.println(sb);






    }
}