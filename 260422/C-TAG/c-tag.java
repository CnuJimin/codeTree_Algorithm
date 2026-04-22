import java.io.*;
import java.util.*;

public class Main {

    static int N, M;
    static HashSet<String> A = new HashSet<>();
    static HashSet<String> B = new HashSet<>();

    static String[][] wordsA;
    static String[][] wordsB;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        wordsA = new String[N][M];
        wordsB = new String[N][M];

        for(int i = 0 ; i < N ; i ++){
            String[] input = br.readLine().split("");
            for(int j = 0 ; j < M ; j ++){
                wordsA[i][j] = input[j];
            }
        }

        for(int i = 0 ; i < N ; i ++){
            String[] input = br.readLine().split("");
            for(int j = 0 ; j < M ; j ++){
                wordsB[i][j] = input[j];
            }
        }

        int cnt = 0;
        for(int i = 0 ; i < M ; i ++){
            for(int j = i + 1 ; j < M ; j ++) {
                for (int k = j + 1 ; k < M ; k ++){
                    A.clear();
                    B.clear();

                    for(int l = 0 ; l < N ; l ++){
                        A.add(wordsA[l][i] + wordsA[l][j] + wordsA[l][k]);
                        B.add(wordsB[l][i] + wordsB[l][j] + wordsB[l][k]);
                    }

                    if(checkA() && checkB()) cnt ++;
                }
            }
        }

        System.out.println(cnt);

    }

    public static boolean checkA(){
        for(String word : A){
            if(B.contains(word)) return false;
        }
        return true;
    }

    public static boolean checkB(){
        for(String word : B){
            if(A.contains(word)) return false;
        }
        return true;
    }

}