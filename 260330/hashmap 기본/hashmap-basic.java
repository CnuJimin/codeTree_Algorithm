import java.util.*;
import java.io.*;

public class Main {

    static HashMap<Integer, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        while(N -- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if(command.equals("add")) add(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            else if (command.equals("find")) System.out.println(find(Integer.parseInt(st.nextToken())));
            else if (command.equals("remove")) remove(Integer.parseInt(st.nextToken()));
        }
    }

    static void add(int a, int b){
        map.put(a,b);
    }

    static void remove(int a){
        map.remove(a);
    }

    static String find(int k){
        if(map.containsKey(k)) return String.valueOf(map.get(k));
        else return "None";
    }
}