#include "Bridges.h"
#include "Array1D.h"

using namespace bridges;

int main(int argc, char **argv) {

	// create Bridges object, set credentials
#if TESTING
	// command line args provide credentials and server to test on
	Bridges bridges (atoi(argv[1]), argv[2], argv[3]);
	if (argc > 4)
		bridges.setServer(argv[4]);
#else
	Bridges bridges (YOUR_ASSSIGNMENT_NUMBER, "YOUR_USER_ID", "YOUR_API_KEY");
#endif
	// set title
	bridges.setTitle("A One-Dimensional Array Example");

	// set description
	bridges.setDescription("Create a 1 dimensional array with integer values and display them");

	// create, populate the array
	Array1D<int> arr (10);

	// populate the array, with squares of indices
	for (int j = 0; j < 10; j++) {
		arr[j] = j * j;

		// use the array values to label the elements
		arr.getElement(j).setLabel(to_string(arr[j]));
	}

	// provide BRIDGES a handle to the data structure
	bridges.setDataStructure(&arr);

	// visualize
	bridges.visualize();

	return 0;
}
