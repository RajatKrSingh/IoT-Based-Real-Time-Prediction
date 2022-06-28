# IoT Based Real Time Prediction
Decentralized MQTT server configured with real-time prediction capabilities built on Hidden Markov Models. Raspberry Pi connected with sensors for transmission to server. Real Time Notification Capabilities Provided.

### MQTT Protocol
MQTT (MQ Telemetry Transport or Message Queue Telemetry Transport) is an ISO standard publish–subscribe based lightweight messaging protocol used on top of the TCP/IP protocol. The main advantage of using this protocol is the minimal network bandwidth requirements. In contrast to the client-server paradigm where the server runs continually to service the client/s, the publish-subscribe approach uses a message broker for distributing messages to interested clients. Instead of initiating connections to specific nodes, information is published and interested parties may subscribe to it. The publish-subscribe paradigm also aims to achieve a scalable multicast, which greatly increases network’s efficiency for content delivery when the same content is requested by multiple subscribers. The network also makes sure that subscribers only receive the information they are interested in, effectively preventing most of SPAM and DoS attacks.

### Implementation Background
<ul>
<li>Our experimental setup consists of multiple sensors(temperature,motion,etc) which are interfaced with a RaspberryPi. We configure a Mosquitto broker to receive sensor readings via the publish/subscribe paradigm. We have a central analytics program which is run on a different server with real time notification capabilities.
<li> Our prediction engine utilizes Hidden Markov Models to identify patterns/aberrations in the sensor readings and alert management. We use a preprocessing of filtering and smoothening to get rid of unwanted noise. Hidden Markov Models are an extension of Markov Chanins where each observable is statistically bound to a hidden state, which have probablistic tarnsition criterias.
<div align="center">
<img src="https://i.imgur.com/Z7HvIVT.png">
</div>
The model shown is defined by the following parameters :-<br>
&nbsp;Hidden States  =  ( 'S1' ,  'S2' )<br>
&nbsp;Observations  =  ( 'No Noise'  ,   'Noise 1'  ,   'Noise 2')<br>
  &nbsp;Start_Probability = {  'S1': 0.6,   'S2': 0.4  }<br>
  &nbsp;Transition_Probability = {<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'S1' : {  'S1': 0.7  ,   'S2': 0.3  },<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'S2' : {  'S1': 0.4  ,   'S2': 0.6},<br>
 &nbsp;&nbsp;}<br>
Emission_probability = {<br>
   		'S1' : {  'No Noise': 0.1  ,   'Noise 1': 0.4  ,   'Noise 2': 0.5},<br>
   		'S2' : {  'No Noise': 0.6  ,   'No Noise': 0.3  ,   'Noise 2': 0.1},<br>
   }<br>
<li> For simulation purposes, we train our statistical model on patterns such as Double Top, Double Bottom, Head & Shoulder and Inverted Head and Shoulder. For each of the patterns we wish to create a HMM model capable of identifying the pattern with a high probability. Using an ensemble of models, we can output the current state with a high degree of confidence.
<div align="center">
  <img src="https://i.imgur.com/G91THaR.png" width=400px>
</div>
<li> Software stack used includes Python, PHP, Arduino and Javascript.
</ul>

### Results

Our analytics framework yielded an accuracy of 97% when test set was limited to reference patterns(one of the patterns on which model is trained on).
<div align="center">
  <img src="https://i.imgur.com/ulpo5kY.png" width=400px>
</div>
When 89 random patterns were added to simulate real time data, the accuracy deteriorated to 93%. These non-reference observation sequences lead to some false positives which lead to a performance deterioration. <br>
<div align="center">
  <img src="https://i.imgur.com/xe0K7Qt.png" width=400px>
</div>
