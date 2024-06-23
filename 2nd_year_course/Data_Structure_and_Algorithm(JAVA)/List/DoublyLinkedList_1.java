package algorithm;

public class DoublyLinkedList_1 {
    /*
        <Doubly Linked List>

        - 일반적인 linked list와 다르게 이전 노드를 가리키는 prev pointer도 가지고 있음.


                                                 Tail
                        Node                       ↑
        +-------+    +-------+    +-------+    +-------+
        | |   | | -> | |   | | -> | |   | | -> | |   | |
        | |   | | <- | |   | | <- | |   | | <- | |   | |
        +-------+    +-------+    +-------+    +-------+
           ↓
          Head

        - head와 tail node를 가지고 시작(더미 노드)



        - 데이터 추가
            - tail dummy node의 앞에 데이터를 추가


        - 검색 by index
            - head나 tail에서 해당 index에 가까운 쪽에서 부터 접근해서 검색


        - 데이터 추가 by index
            1) head나 tail에서 해당 index에 가까운 쪽에서 부터 탐색
            2) index 위치의 node가 'curr node'가 됨
            3) curr node 이전 node인 prev node의 next pointer가 new Node()를, new Node()의 prev pointer가 prev node를,
            new Node()의 next pointer가 curr node를, curr node의 prev pointer가 new Node()를 가리키게 변경


                       new Node()
                      +----------+
                      | |      | |
                      | |      | |
                      +----------+
                     | ↑       ↑ |
                     | |       | |
                     ↓ |       | ↓
            +----------+        +----------+
            | |      | | --//-> | |      | |
            | |      | | <-//-- | |      | |
            +----------+        +----------+
             prev node            curr node



        - 데이터 삭제 by index
            - 삭제하고자 하는 node의 index가 curr node일 때, 이전 노드인 prev node와 다음 노드인 next노드를 서로 연결
            (이 때, curr의 연결들은 모두 끊어줌)


     */
}
