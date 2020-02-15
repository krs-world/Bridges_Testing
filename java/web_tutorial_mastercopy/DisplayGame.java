import bridges.games.*;
import bridges.base.*;

class DisplayGame extends NonBlockingGame {
    public DisplayGame(int assignmentnumber, String username, String apikey) {
        super (assignmentnumber, username,  apikey, 10, 10);

	//this created a game board of 10x10 into assignment 1
    }

    public void initialize() {
	for (int i=0; i<getBoardHeight(); ++i)
	    for (int j=0; j<getBoardWidth(); ++j)
		setBGColor(i, j, NamedColor.ivory);
	
	drawSymbol(1, 1, NamedSymbol.H, NamedColor.blue);
	drawSymbol(1, 2, NamedSymbol.E, NamedColor.yellow);
	drawSymbol(1, 3, NamedSymbol.L, NamedColor.black);
	drawSymbol(1, 4, NamedSymbol.L, NamedColor.green);
	drawSymbol(1, 5, NamedSymbol.O, NamedColor.red);
    }

    public void gameLoop() {
	//This function is executed each frame of the game
    }

    public static void  main (String args[]) {
#if TESTING
    DisplayGame g = new DisplayGame(Integer.parseInt(args[0]), args[1], args[2]);
#else
    DisplayGame g = new DisplayGame(YOUR_ASSIGNMENT_NUMBER, "YOUR_USER_ID",
			"YOUR_API_KEY");
#endif
	g.start();
    }
}
