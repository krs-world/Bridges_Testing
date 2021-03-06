#include <iostream>
#include <string>
#include "Array.h"
#include "Bridges.h"

using namespace std;
using namespace bridges;

int main(int argc, char **argv) {
                        // command line args provide credentials and server to test on
    Bridges *bridges =  new Bridges(atoi(argv[1]), argv[2], argv[3]);
    if (argc > 4)
        bridges->setServer(argv[4]);

	if (argc == 4)		// Server type provided
		bridges->setServer(argv[3]);
		
	Array<string> *arr = new Array<string>(4, 4, 4);

	arr->getElement(0, 0, 0).getVisualizer()->setColor(Color("red"));
	arr->getElement(0, 3, 0).getVisualizer()->setColor(Color("green"));
	arr->getElement(3, 0, 0).getVisualizer()->setColor(Color("blue"));
	arr->getElement(3, 3, 0).getVisualizer()->setColor(Color("magenta"));
	arr->getElement(1, 1, 0).getVisualizer()->setColor(Color("cyan"));
	arr->getElement(2, 2, 0).getVisualizer()->setColor(Color("yellow"));

	bridges->setTitle("3D Array Example");
	bridges->setDataStructure(arr);
	bridges->visualize();

	return 0;
}
