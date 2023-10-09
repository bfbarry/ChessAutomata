output: game.o pieces.o
	echo "hi"
	g++ -std=c++14 -stdlib=libc++ game.o pieces.o -o main.out

game.o: game.cpp
	g++ -std=c++14 -stdlib=libc++ -c game.cpp

pieces.o: pieces.cpp pieces.h
	g++ -std=c++14 -stdlib=libc++ -c pieces.cpp

clean:
	rm *.o
# target: dependencies
# 	<action> 