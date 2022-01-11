## Robot Systems Studies Issue 2

授業内で作成したノードを理解した上で簡単な改良を加えました。


## Demo video


## How to use

1. $ git clone git@github.com:Koukip/Rkadai.git

2. $ cd catkin_ws/src/mypkg/scripts

3. $roscore で別のホームからroscoreを立ち上げておく。


### Operation check　(count.py)

1. 別のホームを作成する。

3. $ rosrun mypkg count.py

4. 元のホームに戻る。

5. $ rostopic echo /count_up


### Operation check (twice.py)

1. 別のホームを作成する。

2. rosrun mypkg twice.py 

3. 元のホームに戻る。

4. $rostopic echo /twice



## License
