import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        TreeSet<Integer> treeSet = new TreeSet<>();

        while(N -- > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if(command.equals("add")){
                int val = Integer.parseInt(st.nextToken());
                if(!treeSet.contains(val)) treeSet.add(val);
            }
            if(command.equals("largest")){
                if(treeSet.isEmpty()){
                    System.out.println("None");
                }else{
                    System.out.println(treeSet.last());
                }
            }
            if(command.equals("smallest")){
                if(treeSet.isEmpty()){
                    System.out.println("None");
                }else{
                    System.out.println(treeSet.first());
                }
            }
            if(command.equals("find")){
                if(treeSet.contains(Integer.parseInt(st.nextToken()))){
                    System.out.println("true");
                }else{
                    System.out.println("false");
                }
            }
            if(command.equals("remove")){
                treeSet.remove(Integer.parseInt(st.nextToken()));
            }
            if(command.equals("lower_bound")){
                Integer val = treeSet.ceiling(Integer.parseInt(st.nextToken()));

                System.out.println(val != null ? val : "None");
            }
            if(command.equals("upper_bound")){
                Integer val = treeSet.higher(Integer.parseInt(st.nextToken()));

                System.out.println(val != null ? val : "None");
            }

        }
    }
}