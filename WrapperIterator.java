import java.util.Iterator;

public class WrapperIterator{
	
	public interface FakeVector<T> extends Iterable<T> {
		public T get(int index);
		public void set (int index, T value);
		public int length = 0;
		public void push(T value);
		public T pop();
		public void insert(int index, T value);
	}
	
	public static class Node<T>{
		T value;
		Node<T> next;
		Node<T> prev;
		Node(T val){
			this.value = val;
			this.next = null;
		}
	}
	
	public static class FakeVectorClass<T> implements FakeVector<T>{
		Node<T> head = null;
		Node<T> tail = null;
		FakeVectorClass(){
		}
		
		@Override
		public Iterator<T> iterator() {
			// Define the certain Iterator with two required methods
			return new Iterator<T>(){
				Node<T> currentNode = head;
				
				@Override
				public boolean hasNext(){
					if (currentNode != null)
							return true;
					return false;
				}
				
				@Override
				public T next(){
					T a = currentNode.value;
					currentNode = currentNode.next;
					return a;
				}
			};
		}

		@Override
		public T get(int index) {
			// Get a value of certain index, if doesnot exist return null
			int i = 0;
			Node<T> temp = head;

			while (i < index){
				if (temp == null)
					return null;
				temp = temp.next;
				i++;
			}

			return (T) temp.value;
		}

		@Override
		public void set(int index, T value) { // start from 0
			Node<T> current = this.head;
			if (this.head == null){
				this.head = new Node<T>(null);
				current = this.head;
				current.next = null;
				current.prev = null;
				this.tail = current;
			}
			
			if (index == 0)
				this.head.value = value;
			
			int i = 1;
			
			while (i <= index){
				if (current.next == null){
					current.next = new Node<T>(null);
				}
				i++;
				current = current.next;
			}
			
			current.value = value;
		}
		

		@Override
		public void push(T value) {
			// push a value in the 0 position
			if (this.head == null){
				this.head = new Node<T>(value);
				return;
			}
			Node<T> temp = new Node<T>(value);
			temp.next = this.head;
			this.head = temp;
		}

		@Override
		public T pop() {
			// pop a value from back
			Node<T> temp = this.head;
			if (temp == null)
				return null;
			this.head = this.head.next;
			return (T) temp.value;
		}

		@Override
		public void insert(int index, T value) {
			// insert a value in index
			Node<T> current = this.head;
			if (this.head == null){
				this.head = new Node<T>(null);
				current = this.head;
			}
			
			if (index == 0)
				this.head.value = value;
			
			int i = 1;
			
			while (i <= index){
				if (current.next == null){
					current.next = new Node<T>(null);
				}
				i++;
				current = current.next;
			}
			
			Node<T> temp2 = new Node<T>(value);
			temp2.next = current.next;
			current.next = temp2;
		}

	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void main(String [] args){
		FakeVectorClass Vector1 = new FakeVectorClass();
		for (int i = 0; i<= 10; i++)
			Vector1.push(i*-1);
		for (int i = 11; i<= 19; i++)
			Vector1.set(i, i*10);
		for (int i = 0; i<= 4; i++)
			Vector1.pop();
		for (int i = 0; i<= 4; i++)
			Vector1.push(-2);
		Vector1.insert(10, -99);
		Iterator itr = Vector1.iterator();
		while (itr.hasNext()){
			System.out.println(itr.next());
		}
	}
}
