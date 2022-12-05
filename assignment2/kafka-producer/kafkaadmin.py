from kafka.admin import KafkaAdminClient, NewTopic

def delete_topics(admin, topic):
    admin.delete_topics(topics=[topic])


def create_topics(admin, topic_list):
    admin.create_topics(new_topics=topic_list, validate_only=False)

vm_ip = '34.29.4.111'
                               
# delete_topics(KafkaAdminClient(bootstrap_servers=f"{vm_ip}:9092", 
#                                client_id='assignment2'), 'orders')
# delete_topics(KafkaAdminClient(bootstrap_servers=f"{vm_ip}:9092", 
#                                client_id='assignment2'), 'order_items')                             


if __name__ == '__main__':
    admin_client = KafkaAdminClient(bootstrap_servers=f"{vm_ip}:9092",
                                    client_id='assignment2')  # use your VM's external IP Here!
    topic_list = [NewTopic(name="orders", num_partitions=1, replication_factor=1),
                  NewTopic(name="order_items", num_partitions=1, replication_factor=1)]
    create_topics(admin_client, topic_list)

