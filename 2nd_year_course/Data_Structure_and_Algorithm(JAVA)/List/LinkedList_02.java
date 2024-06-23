package algorithm;

public class LinkedList_02 {
    /*
        더미 노드: 헤드부터 데이터를 넣는 것이 아닌, 헤드 이후 노드부터 데이터를 넣는 것.
            - 장점: 코드 구현에 있어서 간결해짐.
     */

    private int size;
    private Node head; // 헤드 노드

    public MyLinkedList() {
        this.size = 0;
        this.head = new Node(null); // dummy node
    }



    public void add(T t) { // 현재 linked list의 제일 끝에 데이터를 넣는 method
        // 헤드부터 끝까지 pointer를 타고들어가서 데이터를 넣어줌
        Node curr = this.head;
        while (curr.next != null) {
            curr = curr.next; // while 반복문에서 next값(pointer가 가리키는 값)이 null이
            // 될 때까지 current 변수를 바꿔줌. (next가 null이면 마지막 노드)
        }
        Node node = new Node(t); // 마지막 노드까지 오면 노드를 하나 생성
        curr.next = node; // 마지막 노드 다음에 node를 추가
        this.size++; // 전체 크기를 추가한 노드의 값만큼 (1만큼) 늘려줌
    }



    public void insert(int index, T t) {
        if (index > this.size || index < 0) { // index가 배열크기보다 크거나, 음수가 들어올 경우 에러 발생
            throw new IndexOutOfBoundsException();
        }
        Node prev = this.head;
        Node curr = prev.next;

        int i = 0;
        while (i++ < index) { // 데이터를 넣을 index를 찾음
            prev = prev.next;
            curr = curr.next;
        }
        Node node = new Node(t, curr); // 노드 생성
        prev.next = node; // 새로운 node는 current이고, 이는 이전 node인 previous node의 pointer가
        // 가리키는 값(next)
        this.size++;
    }


    public void clear() {
        this.size = 0;
        this.head.next = null; // head가 가리키는 다음 값이 null이 되는 것은 head가 tail과 같아지면서
        // head가 가리키는 node가 없어지는 상태.
    }



    public boolean delete(T t) {
        Node prev = this.head;
        Node curr = prev.next;

        while (curr != null) { // 배열의 끝가지 탐색
            if (curr.data.equals(t)) { // 입력한 t가 curr과 일치하는치 확인
                prev.next = curr.next; // curr이 입력한 t와 일치하면 현재 node(curr)의 이전 node(prev)의 pointer가 curr의 pointer가
                // 가리키는 다음 node를 가리키도록 변경
                curr.next = null; // 현재 node의 pointer는 null을 가리키도록 변경
                // 즉, curr이 입력 데이터 t와 일치하면 curr이전 node인 prev가 curr의 다음 node를 가리키게 하고,
                // curr의 pointer는 null을 가리키게하여 배열과 연결을 끊어줌
                this.size--;
                return true;
            }
            prev = prev.next;
            curr = curr.next;
        }
        return false;
    }



    public boolean deleteByIndex(int index) {
        if (index >= this.size || index < 0) { // index가 배열크기보다 크거나, 음수가 들어올 경우 에러 발생
            throw new IndexOutOfBoundsException();
        }
        Node prev = this.head;
        Node curr = prev.next;

        int i = 0;
        while (i++ < index) { // 배열의 처음부터 입력된 index까지 탐색
            prev = prev.next;
            curr = curr.next;
        }
        prev.next = curr.next; // 입력된 index의 현재 node는 curr. 현재 node의 이전 node인 prev의 pointer를
        // curr의 pointer가 가리키는 다음 node로 연결
        curr.next = null; // 현재 node인 curr의 pointer를 null로 지정 -> 배열과 연결 끊어줌
        this.size--;
        return true;
    }


    public T get(int index) {
        if (index >= this.size || index <0){
            throw new IndexOutOfBoundsException();
        }
        Node curr = this.head.next; // node들 간의 pointer를 변경하는게 아니라서 previous node를 선언하지 않음.
        // head node는 더미 노드로 사용하기 때문에 그 다음 노드인 head.next부터 탐색 시작
        int i = 0;
        while (i++ < index) { // index node까지 이동
            curr = curr.next;
        }
        return curr.data;
    }


    public int indexOf(T t) { // 입력 데이터 t의 위치(index) 반환
        Node curr = this.head.next;
        int index = 0;
        while (curr != null) {
            if (t.equals(curr.data)) {
                return index;
            }
            curr = curr.next;
            index++;
        }
        return -1;
    }



    public boolean isEmpty() {
        return this.head.next == null; // head의 다음 node가 null(아무 node에도 연결되어있지 않으면), true 반환
        // head의 다음 node가 존재하면 false 반환
    }



    public boolean contains(T t) {
        Node curr = this.head.next;
        while (curr != null) {
            if (t.equals(curr.data)) {
                return true;
            }
            curr = curr.next;
        }
        return false;
    }



    public int size() {
        return this.size;
    }



    private class Node { // 노드 클래스 생성
        T data; // 데이터를 담을 공간
        Node next; // 다음 노드를 가리키는 포인터

        Node(T data) { // 생성자
            this.data = data;
        }

        Node(T data, Node next) { // 생성자
            this.data = data;
            this.next = next;
        }
    }
}