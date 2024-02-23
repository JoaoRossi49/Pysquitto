import time
import random
import paho.mqtt.client as mqtt
import randomCoordinates

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("Não foi possível publicar sua mensagem")

to_publish_list = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(to_publish_list)
mqttc.connect("localhost")
mqttc.loop_start()
while True:
    latitude = randomCoordinates.DDMLatitudeString()
    longitude = randomCoordinates.DDMLongitudeString()

    coordenadas = latitude+longitude

    msg_info = mqttc.publish(f"coordenadas/{random.randint}", coordenadas, qos=1)
    to_publish_list.add(msg_info.mid)

    while len(to_publish_list):
        time.sleep(0.1)

    msg_info.wait_for_publish()
