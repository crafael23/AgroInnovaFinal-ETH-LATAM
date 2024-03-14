import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { MicroserviceOptions } from '@nestjs/microservices';
import { MqttModule } from './mqtt/mqtt.module';
import { MqttConfig } from './mqtt/Configs/mqttconfig';

async function bootstrapAPP() {
  const app = await NestFactory.create(AppModule);
  app.enableCors();
  await app.listen(3000);
}
async function bootstrapMQTT() {
  const mqtt = await NestFactory.createMicroservice<MicroserviceOptions>(
    MqttModule,
    MqttConfig,
  );
  mqtt.listen();
}

async function bootstrap() {
  await Promise.all([bootstrapAPP(), bootstrapMQTT()]);
}

bootstrap();
