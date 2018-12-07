/**
 * Created by Kalpathi Subramanian 
 * Date : 7/17/2018.
 *
 * krs@uncc.edu
 */
import java.lang.String;
import bridges.connect.Bridges;
import bridges.base.SLelement;
import bridges.base.Color;
import bridges.base.ColorGrid;

/**
 *  This example illustrates the use of the Grid type and its subclass, a ColorGrid.
 *  The example builds  a checkerboard with two different colors
 *
 */

public class color_grid {

	public static void main(String[] args) throws Exception {
		if (args.length < 2)
			throw new IllegalArgumentException("Need to provide user ID and API key as command-line arguments!");

                // This example illustrates using the Bridges color grid
                // We will build a checker grid using two different colors

                                                // initialize BRIDGES
		Bridges bridges = new Bridges (8, args[0], args[1]);
		if (args.length == 3)	// If user provides server
			bridges.setServer(args[2]);
                                                // set title for visualization
		bridges.setTitle("A CheckerBoard Example Using Grid Type");

		int width = 200, height = 200;

		Color blue = new Color("blue");
		Color red = new Color("red");

		ColorGrid cg  = new ColorGrid(width, height, red);

                                                // create a checkerboard pattern
                                                // 10 x 10 grid
		int num_squares_x = 10;
		int num_squares_y = 10;

                                                // compute square dimensions
		int sq_width = width/num_squares_x, sq_height = width/num_squares_y;

		for (int j = 0; j < num_squares_y;  j++)
		for (int k = 0; k < num_squares_x;  k++) {

								// use even/odd value of pixel to 
								// figure out the color of the square
			Boolean x_even = (k%2) == 0;
			Boolean y_even = (j%2) == 0;

			Color col;

			if (y_even)
				col = (x_even) ? red : blue;
			else
				col = (x_even) ? blue : red;

                                        // find the address of the square
			int origin_x = k*sq_width;
			int origin_y = j*sq_height;

                                                // color the square
			for (int y = origin_y; y < origin_y+sq_height; y++)
			for (int x = origin_x; x < origin_x+sq_width; x++)
				cg.set(x, y, col);
		}

			bridges.setDataStructure(cg);

			bridges.visualize();
	}
}
