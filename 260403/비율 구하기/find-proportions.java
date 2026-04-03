import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        TreeMap<String, Integer> tm = new TreeMap<>();

        for (int i = 0 ; i < N ; i ++){
            String word = br.readLine();
            if(tm.containsKey(word)){
                tm.put(word, tm.get(word) + 1);
            }else{
                tm.put(word, 1);
            }
        }

        StringBuilder sb = new StringBuilder();

        Iterator<Entry<String, Integer>> it = tm.entrySet().iterator();

        while(it.hasNext()){
            Entry<String, Integer> entry = it.next();
            
            double val = (double) entry.getValue() * 100 / N;
                sb.append(entry.getKey())
                .append(" ")
                .append(String.format("%.4f", val))
                .append("\n");
        }

        System.out.println(sb);
    }
}