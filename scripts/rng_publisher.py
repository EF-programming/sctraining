#!/usr/bin/env python

import random
import rospy
from training.msg import NumB9

def rng_publisher():
    pub = rospy.Publisher('rng_topic', NumB9, queue_size=10)
    rospy.init_node('rng_publisher', anonymous=True)
    rate = rospy.Rate(0.33)
    while not rospy.is_shutdown():
        num = random.randint(0, 2**45)
        numb9 = inttobase9(num)
        numb9message = NumB9(num, numb9)
        rospy.loginfo(numb9message)
        pub.publish(numb9message)
        rate.sleep()

def inttobase9(val):
    result = ""
    while val:
        val, r = divmod(val, 9)
        result += str(r)
    return int(''.join(reversed(result)))


if __name__ == '__main__':
    try:
        rng_publisher()
    except rospy.ROSInterruptException:
        pass
