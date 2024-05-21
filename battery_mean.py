#def read_adc_mean_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_mean_raw', 'r') as file:
#            adc_mean_raw = int(file.read().strip())
#        return adc_mean_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
#def read_adc_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw', 'r') as file:
#            adc_raw = int(file.read().strip())
#        return adc_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## Usage
#mean_raw_value = read_adc_mean_raw()
#raw_value = read_adc_raw()
#if mean_raw_value is not None:
#    print("Mean raw ADC value:", mean_raw_value)
#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#a = 75000 / (30000 + 75000)
##print("Result:", a)
#
#b = 5 / 1024
##print("Result:", b)
#
#c = raw_value * b
##print("Result:", c)
#
#d = c / a
#print("Result:", d)
#
#result_str_d = str(d)
#truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#print("Result:", truncate_result_d)
#
##e = a / 100
##print("Result:", e)
#
##f = raw_value * e
##print("Result:", f)
#
##result_str_f = str(f)
##truncate_result_f = result_str_f[:result_str_f.find('.') + 3]
##print("Result:", truncate_result_f)

#***********

#import pyttsx3
#
#engine = pyttsx3.init()
#
## Function to read ADC mean raw value
#def read_adc_mean_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_mean_raw', 'r') as file:
#            adc_mean_raw = int(file.read().strip())
#        return adc_mean_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## Function to read ADC raw value
#def read_adc_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw', 'r') as file:
#            adc_raw = int(file.read().strip())
#        return adc_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## LiPo voltage chart for 1S (single cell) battery
#lipo_voltage_chart_1s = {
#    100: 4.20,
#    95: 4.15,
#    90: 4.11,
#    85: 4.08,
#    80: 4.02,
#    75: 3.98,
#    70: 3.95,
#    65: 3.91,
#    60: 3.87,
#    55: 3.85,
#    50: 3.84,
#    45: 3.82,
#    40: 3.80,
#    35: 3.79,
#    30: 3.77,
#    25: 3.75,
#    20: 3.73,
#    15: 3.71,
#    10: 3.69,
#    5: 3.61,
#    0: 3.27
#}
#
## Function to get LiPo battery percentage from voltage
#def get_lipo_percentage(voltage):
#    closest_percentage = min(lipo_voltage_chart_1s, key=lambda x: abs(lipo_voltage_chart_1s[x] - voltage))
#    return closest_percentage
#
## Main program
#raw_value = read_adc_raw()
#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#    a = 75000 / (30000 + 75000)
#    b = 5 / 1024
#    c = raw_value * b
#    d = c / a
#
#    result_str_d = str(d)
#    truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#    print("Truncated voltage:", truncate_result_d)
#
#    truncated_voltage = float(truncate_result_d)
#    lipo_percentage = get_lipo_percentage(truncated_voltage)
#    print("LiPo Battery Percentage:", lipo_percentage, '%')
#    engine.setProperty('voice', 'en-gb')
#    engine.setProperty('rate', 140)
#    engine.say("Battery" + str(lipo_percentage) + " percent")
#    engine.runAndWait()
    
#**********************

#import pyttsx3
#import vlc
#import sys
#from pydub import AudioSegment
#sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
#from play_audio import GTTSA
#
#play_audio = GTTSA()
#engine = pyttsx3.init()
#
## Function to read ADC mean raw value
#def read_adc_mean_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_mean_raw', 'r') as file:
#            adc_mean_raw = int(file.read().strip())
#        return adc_mean_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## Function to read ADC raw value
#def read_adc_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw', 'r') as file:
#            adc_raw = int(file.read().strip())
#        return adc_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## LiPo voltage chart for 1S (single cell) battery
#lipo_voltage_chart_1s = {
#    100: 4.2,
#    95: 4.15,
#    90: 4.11,
#    85: 4.08,
#    80: 4.02,
#    75: 3.98,
#    70: 3.95,
#    65: 3.91,
#    60: 3.87,
#    55: 3.85,
#    50: 3.84,
#    45: 3.82,
#    40: 3.8,
#    35: 3.79,
#    30: 3.77,
#    25: 3.75,
#    20: 3.73,
#    15: 3.71,
#    10: 3.69,
#    5: 3.61,
#    0: 3.27
#}
#
## Function to get LiPo battery percentage from voltage
#def get_lipo_percentage(voltage):
#    closest_percentage = min(lipo_voltage_chart_1s, key=lambda x: abs(lipo_voltage_chart_1s[x] - voltage))
#    return closest_percentage
#
## Main program
#raw_value = None
#for _ in range(1):
#    read_adc_mean_raw()  # Call read_adc_mean_raw() but don't use the result
#    raw_value = read_adc_raw()  # Assign the result of the 7th call of read_adc_raw() to raw_value
#
#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#    a = 75000 / (30000 + 75000)
#    b = 5 / 1024
#    c = raw_value * b
#    d = c / a
#
#    result_str_d = str(d)
#    truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#    print("Truncated voltage:", truncate_result_d)
#
#    truncated_voltage = float(truncate_result_d)
#    lipo_percentage = get_lipo_percentage(truncated_voltage)
#    print("LiPo Battery Percentage:", lipo_percentage, '%')
#    
#    if lipo_percentage < 5:
#        print("Battery charge too low, please charge")
#        play_audio.play_machine_audio("battery_charge_too_low_please_charge.mp3")
#        
#    else:
#        engine.setProperty('voice', 'en-gb')
#        engine.setProperty('rate', 140)
#        engine.say("Battery" + str(lipo_percentage) + " percent")
#        engine.runAndWait()

#******************************************************

#import pyttsx3
#import vlc
#import sys
#from pydub import AudioSegment
#sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
#from play_audio import GTTSA
#
#play_audio = GTTSA()
#engine = pyttsx3.init()
#
## Function to read ADC raw value
#def read_adc_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw', 'r') as file:
#            adc_raw = int(file.read().strip())
#        return adc_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## Function to get LiPo battery percentage from voltage range
#def get_lipo_percentage(truncated_voltage):
#    if truncated_voltage >= 4.01:
#        return 100
#    elif 4.00 <= truncated_voltage <= 3.86:
#        return 75
#    elif 3.85 <= truncated_voltage <= 3.71:
#        return 50
#    elif 3.70 <= truncated_voltage <= 3.31:
#        return 25
#    elif 3.30 <= truncated_voltage:
#        return 10
#
## Main program
#raw_value = None
#for _ in range(1):
#    raw_value = read_adc_raw()  # Assign the result of the 7th call of read_adc_raw() to raw_value
#
#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#    a = 75000 / (30000 + 75000)
#    b = 5 / 1024
#    c = raw_value * b
#    d = c / a
#
#    result_str_d = str(d)
#    truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#    print("Truncated voltage:", truncate_result_d)
#
#    truncated_voltage = float(truncate_result_d)
#    print(truncated_voltage)
#    lipo_percentage = get_lipo_percentage(truncated_voltage)
#    print("LiPo Battery Percentage:", lipo_percentage, '%')
#    
#    if lipo_percentage <= 10:
#        print("Battery charge too low, please charge")
#        play_audio.play_machine_audio("battery_charge_too_low_please_charge.mp3")
#        
#    else:
#        engine.setProperty('voice', 'en-gb')
#        engine.setProperty('rate', 140)
#        engine.say("Battery " + str(lipo_percentage) + " percent")
#        engine.runAndWait()

#**********************************************

#import pyttsx3
#import vlc
#import sys
#from pydub import AudioSegment
#sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
#from play_audio import GTTSA
#
#play_audio = GTTSA()
#engine = pyttsx3.init()
#
## Function to read ADC raw value
#def read_adc_raw():
#    try:
#        with open('/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw', 'r') as file:
#            adc_raw = int(file.read().strip())
#        return adc_raw
#    except FileNotFoundError:
#        print("File not found.")
#        return None
#
## Function to get LiPo battery percentage from voltage range
#def get_lipo_percentage(truncated_voltage):
#    if truncated_voltage >= 4.01:
#        return 100
#    elif 3.86 <= truncated_voltage < 4.01:
#        return 75
#    elif 3.71 <= truncated_voltage < 3.86:
#        return 50
#    elif 3.31 <= truncated_voltage < 3.71:
#        return 25
#    else:
#        return 10
#
## Main program
#raw_value = None
#for _ in range(1):
#    raw_value = read_adc_raw()  # Assign the result of the 7th call of read_adc_raw() to raw_value
#
#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#    a = 75000 / (30000 + 75000)
#    b = 5 / 1024
#    c = raw_value * b
#    d = c / a
#
#    result_str_d = str(d)
#    truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#    print("Truncated voltage:", truncate_result_d)
#
#    truncated_voltage = float(truncate_result_d)
#    lipo_percentage = get_lipo_percentage(truncated_voltage)
#    print("LiPo Battery Percentage:", lipo_percentage, '%')
#
#    if lipo_percentage <= 10:
#        print("Battery charge too low, please charge")
#        play_audio.play_machine_audio("battery_charge_too_low_please_charge.mp3")
#
#    else:
#        engine.setProperty('voice', 'en-gb')
#        engine.setProperty('rate', 140)
#        engine.say("Battery " + str(lipo_percentage) + " percent")
#        engine.runAndWait()
        
#************************************

#import pyttsx3
import subprocess
#import sys
#from pydub import AudioSegment
#sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
#from play_audio import GTTSA
#
#play_audio = GTTSA()
#engine = pyttsx3.init()

# Function to read ADC mean raw value
def read_adc_mean_raw():
    try:
        result = subprocess.run(['cat', '/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_mean_raw'], capture_output=True, text=True)
        adc_mean_raw = int(result.stdout.strip())
        print(adc_mean_raw)
        return adc_mean_raw
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
        return None
    except ValueError as e:
        print("Error converting output to integer:", e)
        return None

# Function to read ADC raw value
#def read_adc_raw():
#    try:
#        result = subprocess.run(['cat', '/sys/bus/platform/drivers/meson-saradc/ff809000.adc/iio:device0/in_voltage0_raw'], capture_output=True, text=True)
#        adc_raw = int(result.stdout.strip())
#        return adc_raw
#    except subprocess.CalledProcessError as e:
#        print("Error executing command:", e)
#        return None
#    except ValueError as e:
#        print("Error converting output to integer:", e)
#        return None
#
## Function to get LiPo battery percentage from voltage range
#def get_lipo_percentage(truncated_voltage):
#    if truncated_voltage >= 4.01:
#        return 100
#    elif 3.86 <= truncated_voltage < 4.01:
#        return 75
#    elif 3.71 <= truncated_voltage < 3.86:
#        return 50
#    elif 3.31 <= truncated_voltage < 3.71:
#        return 25
#    else:
#        return 10

# Main program
#raw_value = None
#for _ in range(1):
read_adc_mean_raw()
#    raw_value = read_adc_raw()  # Assign the result of the 7th call of read_adc_raw() to raw_value

#if raw_value is not None:
#    print("Raw ADC value:", raw_value)
#
#    a = 75000 / (30000 + 75000)
#    b = 5 / 1024
#    c = raw_value * b
#    d = c / a
#
#    result_str_d = str(d)
#    truncate_result_d = result_str_d[:result_str_d.find('.') + 3]
#    print("Truncated voltage:", truncate_result_d)
#
#    truncated_voltage = float(truncate_result_d)
#    lipo_percentage = get_lipo_percentage(truncated_voltage)
#    print("LiPo Battery Percentage:", lipo_percentage, '%')
#
#    if lipo_percentage <= 10:
#        print("Battery charge too low, please charge")
#        play_audio.play_machine_audio("battery_charge_too_low_please_charge.mp3")
#
#    else:
#        engine.setProperty('voice', 'en-gb')
#        engine.setProperty('rate', 140)
#        engine.say("Battery " + str(lipo_percentage) + " percent")
#        engine.runAndWait()
