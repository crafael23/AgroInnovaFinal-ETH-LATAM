import { TypeormsqliteService } from './../typeormsqlite/typeormsqlite.service';
import { Controller } from '@nestjs/common';
import {
  Ctx,
  MessagePattern,
  MqttContext,
  Payload,
} from '@nestjs/microservices';
import { ModuleDTO } from './MqttDTOs/ModuleDto';
import { moduleAguaDTO } from './MqttDTOs/moduleAguaDTO';

@Controller('mqtt')
export class MqttController {
  constructor(private typeORMsqlite: TypeormsqliteService) {}

  @MessagePattern('modulo/status')
  executeSaveModulo(
    @Payload() payload: ModuleDTO,
    @Ctx() context: MqttContext,
  ) {
    console.log(`___New message ${context.getTopic()}____`);
    console.log('Payload: ', payload);
    this.typeORMsqlite.CreateModule(payload);
  }

  @MessagePattern('pump/status')
  executeSave(@Payload() payload: any, @Ctx() context: MqttContext) {
    console.log(`___New message ${context.getTopic()}____`);
    console.log('Payload: ', payload);
  }

  @MessagePattern('waterModule/status')
  executeSaveWaterModule(
    @Payload() payload: moduleAguaDTO,
    @Ctx() context: MqttContext,
  ) {
    console.log(`___New message ${context.getTopic()}____`);
    console.log('Payload: ', payload);
    this.typeORMsqlite.CreateModuleAgua(payload);
  }
}
