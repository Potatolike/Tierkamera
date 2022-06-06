# Tierkamera
A little webcam to watch little animals.
It runs on the CrealityBox that was "optimized" to run OpenWRT.
There's a nice tutorial to run OctoWRT on the Creality Box that already precompiles drivers for a webcam.

After setting up MJPG-Streamer I coded a little flask server that uses the functionalities of MJPG-Streamer to take pictures and save them.

The pictures are saved in the static folder.
