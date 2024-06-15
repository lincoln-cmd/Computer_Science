package algorithm;

public class LinkedList_1 {
    /*
        <LinkedList>

                                           Tail
                    Node                    ↑
        +-----+    +-----+    +-----+    +-----+
        |   | | -> |   | | -> |   | | -> |   | | -> Null
        +-----+    +-----+    +-----+    +-----+
           ↓
          Head

        Head: 가장 앞에 위치한 노드
        Tail: 가장 마지막에 위치한 노드. Tail 다음에는 가리킬 노드가 없기 때문에 Null을 가리킨다.

        Node: 데이터를 저장하는 필드와 다음 노드를 가리키는 next pointer로 구성



        ------------------------------
        - 검색
            - index를 통한 randmo access가 불가
            - next pointer를 통해서만 접근
            - n개의 node로 구성된 linked list의 시간 복잡도는 O(N)


        - 추가
            - Head에서 부터 출발해서 Tail까지 가서 Null을 가리키고있는 포인터에 node 데이터를 추가
            - 시간 복잡도는 O(N)


        - 삽입
            - Array List와 다르게 중간에 데이터를 삽입해도 이후의 데이터를 뒤로 미룰 필요가 없음
            - pointer를 변경해주면 됨
            - Head에 데이터를 삽입하면 Head의 pointer만 설정하면 돼서 간단함
            - 해당 위치까지 찾아가는 시간 복잡도는 O(N)


        - 삭제
            - 삭제하고자 하는 node의 next pointer를 아무 것도 가리키지 않게 하고,
            자신을 기리키던 이전 node의 next pointer를 원래 자신이 가리키던 다음
            node를 가리키게 함
            - 아무것도 가리키지 않는 node는 garbage collector가 수거해 삭제됨
            - next pointer를 제대로 설정해 주지 않으면, 연결되지 않은 뒤쪽의 node들이
            모두 삭제될 수 있음
            - 찾아가는 과정에서 시간 복잡도는 O(N) / 삭제 과정 자체는 O(1)



        ------------------------------
        - 장점
            - 배열의 복사나 재할당 없이 데이터 추가 가능
            - 유연한 공간

        - 단점
            - 데이터 접근에 대한 시간이 늘어남

     */

}
