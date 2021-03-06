#include "Bridges.h"
#include "DataSource.h"
#include "Array.h"
#include "SLelement.h"


using namespace bridges;

/*
 * Case Sensitive Implementation of endsWith()
 * It checks if the string 'mainStr' ends with given string 'toMatch'
 *
 * From: http://thispointer.com/c-how-to-check-if-a-string-ends-with-an-another-given-string/
 */
bool endsWith(const std::string &mainStr, const std::string &toMatch) {
	if (mainStr.size() >= toMatch.size() &&
		mainStr.compare(mainStr.size() - toMatch.size(), toMatch.size(), toMatch) == 0)
		return true;
	else
		return false;
}

void setProperties(SLelement<EarthquakeUSGS>* el) {
	/* Get the magnitude of the earthquake from the SLelement
	 *   (the EarthquakeUSGS object is stored as the value inside the SLelement)
	 */
	double magnitude = el->getValue().getMagnitude();

	/* Prepare color and size variables */
	std::string color = "";
	float size = 0.0f;

	/* Pick the color depending on the magnitude */
	if (magnitude < 1.0) {
		color = "blue";
	}
	else if (magnitude < 2.0) {
		color = "green";
	}
	else if (magnitude < 3.0) {
		color = "yellow";
	}
	else if (magnitude < 4.0) {
		color = "orange";
	}
	else if (magnitude < 5.0) {
		color = "red";
	}
	else if (magnitude < 6.0) {
		color = "purple";
	}
	else {
		color = "black";
	}

	auto vizp = el->getVisualizer();

	/* Set the color of the Element */
	vizp->setColor(color);

	/* Set the size of the Element based on the magnitude */
	vizp->setSize(magnitude * 5);

	/* Set the shape of the Element based on the location */
	if (endsWith ( el->getValue().getLocation(), "Alaska")) {
		vizp->setShape(STAR);
	}
	if (endsWith (el->getValue().getLocation(), "Hawaii")) {
		vizp->setShape(WYE);
	}

}

int main(int argc, char **argv) {

	//create the Bridges object, set credentials
#if TESTING
	// command line args provide credentials and server to test on
	Bridges bridges (atoi(argv[1]), argv[2], argv[3]);
	if (argc > 4)
		bridges.setServer(argv[4]);
#else
	Bridges bridges(YOUR_ASSSIGNMENT_NUMBER, "YOUR_USER_ID",
		"YOUR_API_KEY");
#endif


	bridges.setTitle("Linked List with Earthquake Data");

	//Get Earthquake data
	DataSource ds (&bridges);
	std::vector< EarthquakeUSGS > eqs = ds.getEarthquakeUSGSData(500);

	//Building linked list
	SLelement<EarthquakeUSGS>* head = nullptr;

	for (auto eq : eqs) {
		SLelement<EarthquakeUSGS>* newone = new SLelement<EarthquakeUSGS> (eq,
			eq.getTitle());
		newone->setNext(head);
		head = newone;
	}

	//Setting properties.
	{
		SLelement<EarthquakeUSGS>* current = head;
		while (current != nullptr) {
			setProperties(current);
			current = current->getNext();
		}
	}

	// tell Bridges what data structure to visualize
	bridges.setDataStructure(head);

	// visualize the list
	bridges.visualize();

	//free memory
	while (head != nullptr) {
		auto next = head->getNext();
		delete head;
		head = next;
	}

	return 0;
}
