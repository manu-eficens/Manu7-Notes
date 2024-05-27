
# kafka with reverse proxy server
https://www.cloudkarafka.com/docs/kafkarestproxy.html
# kafka documentation 
sudo su -
apt-get update
apt-get install -y wget net-tools netcat tar openjdk-8-jdk
wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz 
tar -xzf kafka_2.13-3.6.1.tgz 
ln -s kafka_2.13-3.6.1 kafka
mkdir zookeeper
cd ~/kafka/config/
vi zookeeper.properties

dataDir=/root/zookeeper
clientPort=2181
maxClientCnxns=0

------------------------------------------
# kafka with reverse proxy server
https://www.cloudkarafka.com/docs/kafkarestproxy.html
# kafka documentation 
sudo su -
apt-get update
apt-get install -y wget net-tools netcat tar openjdk-8-jdk
wget https://downloads.apache.org/kafka/3.6.2/kafka_2.13-3.6.2.tgz 
tar -xzf kafka_2.13-3.6.2.tgz 
ln -s kafka_2.13-3.6.2 kafka
mkdir zookeeper
cd ~/kafka/config/
vi zookeeper.properties

dataDir=/root/zookeeper
clientPort=2181
maxClientCnxns=0

vi zookeeper.properties
-------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# the directory where the snapshot is stored.
dataDir=/root/zookeeper
# the port at which the clients will connect
clientPort=2181
# disable the per-ip limit on the number of connections since this is a non-production config
maxClientCnxns=0
# Disable the adminserver by default to avoid port conflicts.
# Set the port to something non-conflicting if choosing to enable this
admin.enableServer=false
# admin.serverPort=8078
tickTime=2000
#dataDir=/var/lib/zookeeper
#clientPort=2181
initLimit=5
syncLimit=2


rm -rf server.properties
---------------------------------------
vi server.properties
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# see kafka.server.KafkaConfig for additional details and defaults


############################# Server Basics #############################


# The id of the broker. This must be set to a unique integer for each broker.
broker.id=0


############################# Socket Server Settings #############################


# The address the socket server listens on. It will get the value returned from
# java.net.InetAddress.getCanonicalHostName() if not configured.
#   FORMAT:
#     listeners = listener_name://host_name:port
#   EXAMPLE:
#     listeners = PLAINTEXT://your.host.name:9092
advertised.listeners=PLAINTEXT://ip:9092
zookeeper.connect=ip:2181



# Maps listener names to security protocols, the default is for them to be the same. See the config documentation for more details
#listener.security.protocol.map=PLAINTEXT:PLAINTEXT,SSL:SSL,SASL_PLAINTEXT:SASL_PLAINTEXT,SASL_SSL:SASL_SSL


# The number of threads that the server uses for receiving requests from the network and sending responses to the network
num.network.threads=3


# The number of threads that the server uses for processing requests, which may include disk I/O
num.io.threads=8


# The send buffer (SO_SNDBUF) used by the socket server
socket.send.buffer.bytes=102400


# The receive buffer (SO_RCVBUF) used by the socket server
socket.receive.buffer.bytes=102400


# The maximum size of a request that the socket server will accept (protection against OOM)
socket.request.max.bytes=104857600


auto.create.topics.enable=false


############################# Log Basics #############################


log.dirs=/home/ubuntu/kafka-logs


# The default number of log partitions per topic. More partitions allow greater
# parallelism for consumption, but this will also result in more files across
# the brokers.
num.partitions=1


# The number of threads per data directory to be used for log recovery at startup and flushing at shutdown.
# This value is recommended to be increased for installations with data dirs located in RAID array.
num.recovery.threads.per.data.dir=1


############################# Internal Topic Settings  #############################
# The replication factor for the group metadata internal topics "__consumer_offsets" and "__transaction_state"
# For anything other than development testing, a value greater than 1 is recommended for to ensure availability such as 3.
offsets.topic.replication.factor=1
transaction.state.log.replication.factor=1
transaction.state.log.min.isr=1


############################# Log Flush Policy #############################


# Messages are immediately written to the filesystem but by default we only fsync() to sync
# the OS cache lazily. The following configurations control the flush of data to disk.
# There are a few important trade-offs here:
#    1. Durability: Unflushed data may be lost if you are not using replication.
#    2. Latency: Very large flush intervals may lead to latency spikes when the flush does occur as there will be a lot of data to flush.
#    3. Throughput: The flush is generally the most expensive operation, and a small flush interval may lead to exceessive seeks.
# The settings below allow one to configure the flush policy to flush data after a period of time or
# every N messages (or both). This can be done globally and overridden on a per-topic basis.


# The number of messages to accept before forcing a flush of data to disk
#log.flush.interval.messages=10000


# The maximum amount of time a message can sit in a log before we force a flush
#log.flush.interval.ms=1000


############################# Log Retention Policy #############################


# The following configurations control the disposal of log segments. The policy can
# be set to delete segments after a period of time, or after a given size has accumulated.
# A segment will be deleted whenever *either* of these criteria are met. Deletion always happens
# from the end of the log.


# The minimum age of a log file to be eligible for deletion due to age
log.retention.hours=168


# A size-based retention policy for logs. Segments are pruned from the log unless the remaining
# segments drop below log.retention.bytes. Functions independently of log.retention.hours.
#log.retention.bytes=1073741824


# The maximum size of a log segment file. When this size is reached a new log segment will be created.
log.segment.bytes=1073741824


# The interval at which log segments are checked to see if they can be deleted according
# to the retention policies
log.retention.check.interval.ms=300000


############################# Zookeeper #############################


# Zookeeper connection string (see zookeeper docs for details).
# This is a comma separated host:port pairs, each corresponding to a zk
# server. e.g. "127.0.0.1:3000,127.0.0.1:3001,127.0.0.1:3002".
# You can also append an optional chroot string to the urls to specify the
# root directory for all kafka znodes.


# Timeout in ms for connecting to zookeeper
zookeeper.connection.timeout.ms=6000



############################# Group Coordinator Settings #############################


# The following configuration specifies the time, in milliseconds, that the GroupCoordinator will delay the initial consumer rebalance.
# The rebalance will be further delayed by the value of group.initial.rebalance.delay.ms as new members join the group, up to a maximum of max.poll.interval.ms.
# The default value for this is 3 seconds.
# We override this to 0 here as it makes for a better out-of-the-box experience for development and testing.
# However, in production environments the default value of 3 seconds is more suitable as this will help to avoid unnecessary, and potentially expensive, rebalances during application startup.

--------------------------------------------------------------------------------------------------------------------------------


cd /root

~/kafka/bin/zookeeper-server-stop.sh
~/kafka/bin/zookeeper-server-start.sh -daemon ~/kafka/config/zookeeper.properties
tail -n 10 ~/kafka/logs/zookeeper.out
------------------------------------------
~/kafka/bin/kafka-server-stop.sh
~/kafka/bin/kafka-server-start.sh -daemon ~/kafka/config/server.properties
tail -n 10 ~/kafka/logs/kafkaServer.out

# hemasai for spark stage 
~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --create --topic topic-stage --replication-factor 1 --partitions 8
~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --describe --topic topic-stage
~/kafka/bin/kafka-console-producer.sh --bootstrap-server ip:9092 --topic topic-stage
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic topic-stage --group my-group
-------------------------------------------------------------------------------------------------------------------------------
# hemasai for spark dev approach-2
~/kafka/bin/kafka-topics.sh --bootstrap-server 172.31.3.102:9092 --describe --topic topic-dev
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server 172.31.3.102:9092 --topic topic-dev --group development-group
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server 172.31.3.102:9092 --list
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server 172.31.3.102:9092 --group development-group --describe
------------------------------------------------------------------------------------------
# hemasi final approach
# create consumer group for dev 

~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --describe --topic topic-dev
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic topic-dev --group development-group
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --list
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --group development-group --describe

# create consumer group for stage
~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --describe --topic topic-stage
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic topic-stage --group stage-group
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --list
~/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --group stage-group --describe

# create consumer group for prod
/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --describe --topic topic-prod
/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic topic-prod --group prod-group
/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --list
/kafka/bin/kafka-consumer-groups.sh --bootstrap-server ip:9092 --group prod-group --describe

# roughf work

~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --create --topic demo-topic1 --replication-factor 1 --partitions 2


~/kafka/bin/kafka-console-producer.sh --broker-list ip:9092 --topic demo-topic1


<<<<<<< HEAD
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic demo-topic1

# with load balancer endpoint 
~/kafka/bin/kafka-topics.sh --bootstrap-server spark-dev-kafka-clb-33738784.us-east-1.elb.amazonaws.com:9092 --create --topic demo-topic5 --replication-factor 1 --partitions 2


~/kafka/bin/kafka-console-producer.sh --broker-list ip:9092 --topic demo-topic1


~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic demo-topic1

~/kafka/bin/kafka-topics.sh --bootstrap-server ip:9092 --create --topic demo-topic5 --replication-factor 1 --partitions 2
=======
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server ip:9092 --topic demo-topic1
>>>>>>> 36ec3b6b2679b7815d8a9a2f9a1e4928867ee959
---------------------------------------------------------
# uninstall kafka 
sudo rm -rf /etc/kafka
sudo rm -rf /var/lib/kafka
sudo apt-get remove kafka
ls
rm -rf kafka
rm -rf kafka_2.13-3.6.2
rm -rf kafka_2.13-3.6.2.tgz
ls
rm -rf zookeeper/
sudo find / -name meta.properties
cd /home/ubuntu/
ls
rm -rf kafka-logs


