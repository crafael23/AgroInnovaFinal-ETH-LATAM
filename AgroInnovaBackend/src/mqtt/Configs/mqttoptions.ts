import { MqttOptions, Transport } from '@nestjs/microservices';

export class MqttOptionsConfig implements MqttOptions {
  name: string;
  transport: any;
  options: any;

  constructor() {
    this.name = 'Cliente_NestJS';
    this.transport = Transport.MQTT;
    this.options = {
      subscribeOptions: { qos: 1 },
      url: 'mqtt://localhost:1883',
    };
  }
}
