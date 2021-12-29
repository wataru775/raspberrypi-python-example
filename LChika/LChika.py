#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 使用ポートは21
EXPORT_PORT = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(EXPORT_PORT, GPIO.OUT)

# LEDを光らせる
GPIO.output(EXPORT_PORT, True)
time.sleep(1)
GPIO.output(EXPORT_PORT, False)
time.sleep(1)
GPIO.output(EXPORT_PORT, True)
time.sleep(2)
GPIO.output(EXPORT_PORT, False)
time.sleep(1)
GPIO.output(EXPORT_PORT, True)
time.sleep(3)
GPIO.output(EXPORT_PORT, False)
time.sleep(1)

GPIO.cleanup()