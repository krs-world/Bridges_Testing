import bridges.base.CircDLelement;
import bridges.connect.Bridges;

public class cdllist {

	public static void main(String[] args) throws Exception {


#if TESTING
		Bridges bridges = new Bridges(Integer.parseInt(args[0]), args[1], args[2]);
		bridges.setServer(args[3]);
#else
		Bridges bridges = new Bridges(YOUR_ASSIGNMENT_NUMBER, "YOUR_USER_ID", 
										"YOUR_API_KEY");
#endif
		bridges.setTitle("A Circular Doubly Linked List Example");
        bridges.setDescription("In this example the user has built an array of students and their information including, student number, "
                +   "name, major, email address, favorite color, disliked color, and credit hours. A for loop is used to iterate through this array "
                +   "creating and linking a list of CircDLelements. After the list is created, an enhanced for loop is used to alter the visual "
                +   "attributes of the data using the students color preferences and number of credits.");
				
		StudentInfo[] students = {
			new StudentInfo(
				"00000000000",
				"Gretel Chaney",
				"CS",
				"g.chaney@generated.com",
				"magenta",
				"blue",
				9.0
			),
			new StudentInfo(
				"00000000001",
				"Karol Soderman",
				"SIS",
				"k.soderman@generated.com",
				"magenta",
				"red",
				11.0
			),
			new StudentInfo(
				"00000000002",
				"Lamont Kyler",
				"BIO",
				"l.kyler@generated.com",
				"yellow",
				"green",
				12.0
			),
			new StudentInfo(
				"00000000003",
				"Gladys Serino",
				"CS", "g.serino@generated.com",
				"blue",
				"magenta",
				9.0
			),
			new StudentInfo("00000000004",
				"Starr Mcginn",
				"CS",
				"s.mcginn@generated.com",
				"red",
				"yellow",
				15.0)
		};

		//initializing all student elements
		CircDLelement<StudentInfo> head = null;

		for (int i = 0; i < students.length; i++) {
			if (i > 0)
				head = insertFront(head, new CircDLelement<StudentInfo>("", students[i]));
			else
				head = new CircDLelement<StudentInfo>("", students[i]);
		}

		CircDLelement<StudentInfo> current = head;
		// add visual attributes
		do {
			current.setLabel(current.getValue().getStudentLabel());
			current.getVisualizer().setColor(current.getValue().getFavoriteColor());

			current.getLinkVisualizer(current.getNext()).setColor(current.getValue().getDislikeColor());
			current.getLinkVisualizer(current.getNext()).setThickness(current.getValue().getStudentCreditHours() * .2);

			current.getLinkVisualizer(current.getPrev()).setColor(current.getValue().getDislikeColor());
			current.getLinkVisualizer(current.getPrev()).setThickness(current.getValue().getStudentCreditHours() * .2);

			current = current.getNext();
		}	while (current != head);

		bridges.setDataStructure(head);

		bridges.visualize();
	}

	public static CircDLelement<StudentInfo> insertFront(
		CircDLelement<StudentInfo> tailElement,
		CircDLelement<StudentInfo> newElement) {
		CircDLelement<StudentInfo> tailNextElement = tailElement.getNext();

		newElement.setNext(tailNextElement);
		newElement.setPrev(tailElement);

		tailNextElement.setPrev(newElement);
		tailElement.setNext(newElement);

		return tailElement;
	}
}
