package algorithm;

import java.util.Arrays;

public class MyArrayList<T> {
    // 디폴트 사이즈 설정
    private static final int DEFAULT_SIZE = 50;

    // 멤버 변수
    private int size;
    private T[] elements;


    // 생성자
    public MyArrayList() {
        this.size = 0;
        this.elements = (T[]) new Object[DEFAULT_SIZE];
    }


    public void add(T t) {
        if (this.size == this.elements.length) {
            this.elements = Arrays.copyOf(this.elements, this.size * 2);
        } // 리스트가 꽉 차있을 경우, 배열을 늘려준다.
        // 여기서는 배열을 2배로 늘리고, 기존의 데이터들을 모두 옮겨준다.
        this.elements[this.size] = t;
        this.size++;
    }



    public void insert(int index, T t) {
        if (this.size == this.elements.length) {
            this.elements = Arrays.copyOf(this.elements, this.size * 2);
        }
        for (int i = index; i < this.size; i++) {
            this.elements[i + 1] = this.elements[i];
        } // 기존 index 위치에 있던 데이터를 다음 위치인 index + 1로 이동
        this.elements[index] = t;
        this.size++;
    }



    public void clear() { // 리스트 내부의 모든 데이터를 삭제하고, 초기화
        // 처음에 생성자를 만들 때와 같이 구현
        this.size = 0;
        this.elements = (T[]) new Object[DEFAULT_SIZE];
    }



    public boolean delete(T t) {
        for (int i = 0; i < this.size; i++) {
            if (this.elements[i].equals(t)) { // 타겟과 입력으로 들어온 값(t)가 일치하는지 확인
                for (int j = i; j < this.size - 1; j++) {
                    this.elements[j] = this.elements[j + 1];
                } // 값이 일치하면, 해당 위치(i)에서부터 배열의 끝까지의 값들을 앞으로 이동 시킨다
                this.size--;
                return true; // 삭제 완료시 true를 return
            }
        }
        return false; // 입력 값(t)과 일치하는 값이 없으면 삭제 행동이 실행되지 않으므로 false를 return
    }



    public boolean deleteByIndex(int index) {
        if (index < 0 || index > this.size) {
            return false;
        } // 잘못된 인덱스 값이 들어오면 false를 return
        for (int i = index; i < this.size - 1; i++) {
            this.elements[i] = this.elements[i + 1];
        } // 기존 index 위치에 있던 데이터가 삭제되었으므로,
        // 현재 index로 다음 위치인 index + 1의 데이터를 가져옴
        this.size--;
        return true;
    }



    public T get(int index) {
        if (index < 0 || index > this.size) {
            throw new IndexOutOfBoundsException();
        } // 잘못된 index값이 들어올 경우를 처리
        // 현재 메소드는 return type이 boolean이 아니기 때문에 return false 구문이 아닌,
        // exception을 발생시켜 준다.
        return this.elements[index]; // 입력된 위치 값(index)의 데이터를 반환
    }



    public int indexOf(T t) { // 입력된 값이 배열 내에 존재하면, 해당 위치를 반환
        for (int i = 0; i < this.size; i++) {
            if (this.elements[i].equals(t)) {
                return i;
            }
        }
        return -1;
    }



    public boolean isEmpty() { // 리스트에 데이터가 존재하는지 확인
        // 데이터가 존재하면 false, 존재하지 않고 비어있으면 true를 return
        return this.size == 0;
    }



    public boolean contains(T t) { // 배열 내에 입력된 값이 존재하는지 유무 확인
        for (int i = 0; i < this.size; i++) {
            if (this.elements[i].equals(t)) {
                return true;
            } // 배열을 처음부터 순회하면서 입력값과 일치하면 true 반환
        }
        return false;
    }



    public int size() {
        return this.size;
    }
}