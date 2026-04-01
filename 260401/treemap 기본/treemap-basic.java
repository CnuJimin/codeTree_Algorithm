import java.io.*;
import java.util.*;
import java.util.Map.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        TreeMap<Integer, Integer> map = new TreeMap<>();

        while(N -- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());

            String command = st.nextToken();

            if(command.equals("add")){
                int k = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());
                map.put(k, v);

            }else if(command.equals("find")){
                int k = Integer.parseInt(st.nextToken());
                if(map.containsKey(k)){
                    System.out.println(map.get(k));
                }else{
                    System.out.println("None");
                }
            }else if(command.equals("remove")){
                map.remove(Integer.parseInt(st.nextToken()));

            }else if (command.equals("print_list")){

                if(map.isEmpty()){
                    System.out.println("None");
                    continue;
                }

                Iterator<Entry<Integer, Integer>> it = map.entrySet().iterator();
                while(it.hasNext()){
                    Entry<Integer, Integer> entry = it.next();
                    System.out.print(entry.getValue() + " ");
                }
                System.out.println();

            }
        }
    }
}