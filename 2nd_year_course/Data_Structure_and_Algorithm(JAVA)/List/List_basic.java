package algorithm;

import java.util.ArrayList;
import java.util.List;

public class List_basic {
    public static void main(String[] args) {
        /*
            <List>

            - 선형적인 자료구조
            - 데이터를 일렬로 늘여 놓은 형태
            - 순서


            List에서 중요한 3가지 연산
                - 데이터 삽입
                - 데이터 삭제
                - 데이터 탐색


            List의 구분
                - ArrayList
                - LinkedList
                    - Single LinkedList
                    - Double LinkedList


         */

//-----------------------------------------------------------------------------

        /*
            ArrayList

            - 배열 기반의 리스트
            - 메모리 공간을 연속적으로 사용

         */


        List<String> list = new ArrayList<String>();

        // 데이터 삽입
        // 데이터가 이미 들어있는 리스트의 데이터들 중간에 다른 데이터를 삽입하면,
        // 해당 위치 이후의 데이터들은 뒤로 한칸씩 밀린다. 따라서, 시간 복잡도는 O(N)
        list.add("Hello");
        list.add("Hi");
        list.add("Hola");
        list.add("안녕하세요");

        System.out.println(list);



        // 데이터 삭제
        // 리스트 중간에 있는 데이터를 삭제시, 해당 인덱스 이후의 데이터들이
        // 앞으로 당겨진다. 따라서, 시간복잡도는 O(N)
        list.remove("Hello");

        System.out.println(list);



        // 데이터 탐색
        // 인덱스를 통한 탐색은 시간 복잡도가 O(N)
        // LinkedList의 경우, 인덱스를 통한 탐색이 불가
        System.out.println(list.get(0));
        System.out.println(list.get(2));
    }
}
