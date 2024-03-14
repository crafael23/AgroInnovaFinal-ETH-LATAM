import { Inject, Injectable } from '@nestjs/common';
import { ClientProxy, MqttRecordBuilder } from '@nestjs/microservices';

@Injectable()
export class MqttService {
  constructor(@Inject('Cliente_NestJS') private client: ClientProxy) {}
  sendMqttMessage(topic: string, message: any) {
    const record = new MqttRecordBuilder(message).setQoS(1).build();
    this.client.send(topic, record).subscribe((res) => {
      console.log(`Respuesta del cliente: ${topic} con el valor: ${res}`);
    });
  }
}
