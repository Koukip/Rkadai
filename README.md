## Robot Systems Studies Issue 2

授業内で作成したノードを理解した上で簡単な改良を加えました。


## Demo video

https://youtu.be/K6MbpHZAHEE

## How to use

1. $ git clone git@github.com:Koukip/Rkadai.git

2. $ cd catkin_ws/src/mypkg/scripts

3. $ catkin_make

3. $roscore で別のホームからroscoreを立ち上げておく。


### Operation check　(count.py)

1. 別のホームを作成する。

2. $ rosrun mypkg count.py

3. 元のホームに戻る。

4. $ rostopic echo /count_up

→　nを1ずつ足して10Hzで出される。


### Operation check (twice.py)

1. 別のホームを作成する。

2. rosrun mypkg twice.py 

3. 元のホームに戻る。

4. $rostopic echo /twice

→　数字を3倍にして10Hzで出される。



## License

BSD 3-Clause "New" or "Revised" License

https://github.com/Koukip/Rkadai/blob/2ffcda5d920465559f3429e90565a9c6ceb1e14f/LICENSE
