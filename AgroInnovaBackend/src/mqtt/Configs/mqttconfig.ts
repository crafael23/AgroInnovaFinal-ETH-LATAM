import { MqttOptions, Transport } from '@nestjs/microservices';

export const MqttConfig: MqttOptions = {
  transport: Transport.MQTT,
  options: {
    subscribeOptions: { qos: 1 },
    url: 'mqtt://localhost:1883',
  },
};
