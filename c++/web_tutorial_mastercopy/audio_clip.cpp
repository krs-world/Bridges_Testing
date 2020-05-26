#include "AudioClip.h"
#include <iostream>
#include <fstream>
#include "Bridges.h"
#include <math.h>

using namespace std;
using namespace bridges;

void generateSine(AudioClip * ac) {
    for (int s = 0; s < ac->getSampleCount(); s++) {
        for (int c = 0; c < ac->getNumChannels(); c++) {
            double val = sin(s / 20.0);
            int minmax32 = (pow(2, 32) / 2.0) - 1.0;

            int amp = (int)(val * minmax32);
            
            ac->setSample(c, s, amp);
        }
    }
}

int main(int argc, char*argv[]) {

#if TESTING
	// command line args provide credentials and server to test on
	Bridges bridges (atoi(argv[1]), argv[2], argv[3]);

	if (argc > 4)
		bridges.setServer(argv[4]);


#else
	Bridges bridges (YOUR_ASSSIGNMENT_NUMBER, "YOUR_USER_ID",
		"YOUR_API_KEY");
#endif

    bridges.setTitle("Audio Mixing");
    bridges.setDescription("sine");

    // Load the clips
    AudioClip clip = AudioClip(44100*5, 1, 32, 44100);

    generateSine(&clip);

    bridges.setDataStructure(clip);
    bridges.visualize();

    return 0;
}