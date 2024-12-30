import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int MAX;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] arr = new char[N][N];
        MAX = 0;
        
        for(int i = 0; i  < N; i++) {
        	String str = br.readLine();
        	for(int j = 0; j < N; j++) {
        		arr[i][j] = str.charAt(j);
        	}
        }
        
        for(int i = 0; i < N; i++) {
        	for(int j = 0; j < N - 1; j++) {
        		if(arr[i][j] == arr[i][j+1]) continue;
    			changArrColumn(arr, i, j);
    			checkArr(arr);
    			changArrColumn(arr, i, j);
        	}
        }
        
        for(int i = 0; i < N; i++) {
        	for(int j = 0; j < N - 1; j++) {
        		if(arr[j][i] == arr[j + 1][i]) continue;
        		changArrRow(arr, j, i);
        		checkArr(arr);
        		changArrRow(arr, j, i);
        	}
        }
        
        System.out.println(MAX);
        br.close();   
    }
    
    static void changArrColumn(char[][] arr, int i, int j) {
    	char temp = arr[i][j];
		arr[i][j] = arr[i][j+1];
		arr[i][j+1] = temp;
    }
    
    static void changArrRow(char[][] arr, int i, int j) {
    	char temp = arr[i][j];
		arr[i][j] = arr[i + 1][j];
		arr[i + 1][j] = temp;
    }
    
    static void checkArr(char[][] arr) {
    	int cnt = 0;
    	// 가로 체크
    	for(int i = 0; i < arr.length; i++) {
    		cnt = 1;
    		for(int j = 0; j < arr.length - 1; j++) {
    			if(arr[i][j] == arr[i][j+1]) cnt++;
    			else cnt = 1;
    			if(MAX < cnt) MAX = cnt;
    		}
    	}
    	
    	// 세로 체크
    	for(int i = 0; i < arr.length; i++) {
    		cnt = 1;
    		for(int j = 0; j < arr.length - 1; j++) {
    			if(arr[j][i] == arr[j+1][i]) cnt++;
    			else cnt = 1;
    			if(MAX < cnt) MAX = cnt;
    		}
    	}
    }
}