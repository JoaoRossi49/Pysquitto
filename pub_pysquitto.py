import time
import random
import paho.mqtt.client as mqtt
import randomCoordinates
import datetime

def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print("Não foi possível publicar sua mensagem")

to_publish_list = set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_publish = on_publish

mqttc.user_data_set(to_publish_list)
mqttc.connect("localhost", port=8080)
mqttc.loop_start()

data_inclusao = datetime.datetime.now()

coordenadas_rota66 = [
(41.8781, -87.6298),
(41.8427, -87.2980),
(41.8074, -86.9662),
(41.7720, -86.6344),
(41.7366, -86.3026),
(41.7012, -85.9708),
(41.6659, -85.6390),
(41.6305, -85.3072),
(41.5951, -84.9754),
(41.5597, -84.6436),
(41.5244, -84.3118),
(41.4890, -83.9800),
(41.4536, -83.6482),
(41.4182, -83.3164),
(41.3829, -82.9846),
(41.3475, -82.6528),
(41.3121, -82.3210),
(41.2767, -81.9892),
(41.2414, -81.6574),
(41.2060, -81.3256),
(41.1706, -80.9938),
(41.1352, -80.6620),
(41.0999, -80.3302),
(41.0645, -79.9984),
(41.0291, -79.6666),
(40.9937, -79.3348),
(40.9584, -79.0030),
(40.9230, -78.6712),
(40.8876, -78.3394),
(40.8523, -78.0076)
]

for coordenada in coordenadas_rota66:
    codigo_dispositivo = "ONEP"
    coordenadas = coordenada
    latitude, longitude = coordenadas

    payload = f'{{\"codigo_dispositivo\":\"{codigo_dispositivo}\", \"latitude\":\"{latitude}\", \"longitude\":\"{longitude}\", \"data_inclusao\":\"{data_inclusao}\"}}'
    
    print(payload)

    msg_info = mqttc.publish("/coordenada", str(payload), qos=1)
    to_publish_list.add(msg_info.mid)

    while len(to_publish_list):
        time.sleep(2)

    msg_info.wait_for_publish()
