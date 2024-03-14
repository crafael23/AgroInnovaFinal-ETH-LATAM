import { Module } from '@nestjs/common';
import { ClientsModule } from '@nestjs/microservices';
import { MqttController } from './mqtt.controller';
import { TypeormsqliteModule } from 'src/typeormsqlite/typeormsqlite.module';
import { MqttService } from './mqtt.service';
import { MqttOptionsConfig } from './Configs/mqttoptions';

const mqttoptions = new MqttOptionsConfig();

@Module({
  imports: [ClientsModule.register([mqttoptions]), TypeormsqliteModule],
  controllers: [MqttController],
  providers: [MqttService],
  exports: [MqttService],
})
export class MqttModule {}
