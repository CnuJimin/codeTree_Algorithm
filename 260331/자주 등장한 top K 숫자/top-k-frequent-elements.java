import java.io.*;
import java.util.*;

public class Main {

    static class Pair implements Comparable<Pair>{
        int num;
        int cnt;

        public Pair(int num, int cnt){
            this.num = num;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Pair p){
            if(this.cnt == p.cnt) return Integer.compare(p.num, this.num);
            return Integer.compare(p.cnt, this.cnt);
        }


    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());

        for (int i = 0 ; i < N ; i ++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        HashMap<Integer, Integer> map = new HashMap<>(); // <수, 등장 횟수>

        for (int num : arr){
            if(map.containsKey(num)){
                map.put(num, map.get(num) + 1);
            }else{
                map.put(num, 1);
            }
        }

        List<Pair> list = new ArrayList<>();

        for (int n : map.keySet()){
            list.add(new Pair(n, map.get(n)));
        }

        Collections.sort(list);

        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < K ; i ++){
            sb.append(list.get(i).num).append(" ");
        }

        System.out.println(sb);



    }
}