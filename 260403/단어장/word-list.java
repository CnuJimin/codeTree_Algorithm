import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        TreeMap<String, Integer> map = new TreeMap<>();

        

        while(N -- > 0){
            String word = br.readLine();

            if (!map.containsKey(word)) map.put(word, 1);
            else map.put(word, map.get(word) + 1);
        }

        Iterator<Entry<String, Integer>> it = map.entrySet().iterator();

        while(it.hasNext()){
            Entry<String, Integer> entry = it.next();

            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}