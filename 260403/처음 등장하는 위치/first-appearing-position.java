import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        TreeMap<Integer, Integer> map = new TreeMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1 ; i <= N ; i ++){
            int num = Integer.parseInt(st.nextToken());

            if(!map.containsKey(num)) map.put(num, i);
        }

        Iterator<Entry<Integer, Integer>> it = map.entrySet().iterator();

        StringBuilder sb = new StringBuilder();

        while(it.hasNext()){
            Entry<Integer, Integer> entry = it.next();
            sb.append(entry.getKey()).append(" ").append(entry.getValue()).append("\n");
        }

        System.out.println(sb);
    }
}