package lab02;

class Node
{
	int data;
	Node next;
	public Node( int d,Node n )
	{
		data = d;
		next = n;
	}
}
class Mylist
{
	Node head;
	int total = 0;
	public Mylist() {}
	public Mylist(int[] a)
	{
		int sz = a.length;
		if( sz!=0 )
		{
			head = new Node(a[0],null);
			Node tail = head;
			total++;
			for(int i = 1;i<sz;i++)
			{
				tail.next = new Node(a[i],null);
				tail = tail.next;
				total++;
			}
		}
	}
	public Mylist(Mylist a)
	{
		Node n = a.head;
		if( n!=null )
		{
			head = new Node(n.data,null);
			Node tail = head;
			n = n.next;
			total++;
			while(n!=null)
			{
				tail.next = new Node(n.data,null);
				tail = tail.next;

				n = n.next;
				total++;
			}
		}
	}
	void insert(int i)
	{
		Node n = head;
		if(n==null)
		{
			head = new Node(i,null);
			total++;
			return;
		}
		while(n.next!=null&&n.data!=i)
			n = n.next;
		if(n.data==i)
			return;
		n.next  = new Node(i,null);
		total++;
	}
	void showList( )
	{
		Node n = head;
		if(n==null)
		{
			return;
		}
		while(n!=null) {
			System.out.println( n.data );
			n = n.next;
		}
	}
	boolean isEmpty()
	{ return total==0; }
	void clear()
	{
		if(head==null)
			return;
		head.next = null;
		head = null;
	}
	void insertat(int i,int index)
	{
		if(index>=total || index<0)
			return;
		Node n = head;
		int ind = 0;
		while(ind<index && n.data!=i)
			n = n.next;
		if(n.data==i)
			return;
		Node next_ = n.next;
		n.next = new Node(i,null);
		n.next.next = next_;
		total++;

	}
	Node remove(int di)
	{
		Node ret = null;
		Node n = head;
		if(n==null)
			return null;
		Node prev = null;
		while(n.next!=null && n.data != di) {
			prev = n;
			n = n.next;
		}
		if( n.data==di )
		{
			total--;
			if(prev==null)
			{
				ret = head;
				head = head.next;
				return ret;
			}
			else
			{
				prev.next = n.next;
				n.next = null;
				return n;
			}


		}

		return ret;
	}
}



public class LAB02 {

	static Mylist evens(Mylist l)
	{
		Mylist l1 = new Mylist();
		Node n = l.head;
		if(n==null)
			return null;
		while(n.next!=null)
		{
			if( n.data%2==0 )
				l1.insert(n.data);
			n = n.next;
		}
		return l1;
	}
	static boolean find(Mylist l,int num)
	{
		Node n = l.head;
		if(n==null)
			return false;

		while(n.next!=null)
		{
			if( n.data%2==0 )
				return true;
			n = n.next;
		}

		return false;
	}

	static void reverse_inplace(Mylist l)
	{

		Node n = l.head;
		if(n==null)
			return;
		Node tail = null;
		while(n.next!=null)
			n = n.next;
		tail = n;

		Node newhead = null;
		n = l.head;
		while(n!=null)
		{
			Node nextnode = n.next;
			n.next = newhead;
			newhead = n;
			n = nextnode;
		}

		l.head = newhead;
		Node n_ = l.head;
		while(n_.next!=null)
			n_ = n_.next;
		tail = n_;
		return;
	}


	static void printsum(Mylist l)
	{
		Node n = l.head;
		if(n==null)
			return;
		int sum = 0;
		while(n!=null)
		{
			sum += n.data;
			n = n.next;
		}
		System.out.println(sum);
	}


	public static void main(String[] args)
	{


		int a1[] = {10,20,30,40};
		Mylist l1 = new Mylist();

		l1.insert(11);
		l1.insert(11);
		l1.insert(21);
		l1.insert(21);
		l1.insert(31);
		l1.insert(41);

		l1.showList();
		System.out.println("l1 has total "+l1.total+" elements");

		Mylist l2 = new Mylist(a1);
		Mylist l3 = new Mylist(l1);

		l2.showList();
		System.out.println("l2 has total "+l2.total+" elements");

		l3.showList();
		System.out.println("l3 has total "+l3.total+" elements");

		reverse_inplace(l3);
		l3.showList();
		System.out.println("l3 has total "+l3.total+" elements");
	}
}
