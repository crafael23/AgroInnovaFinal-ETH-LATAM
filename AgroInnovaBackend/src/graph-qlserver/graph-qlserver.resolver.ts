import {
  Args,
  Query,
  Resolver,
  Int,
  Mutation,
  Subscription,
} from '@nestjs/graphql';
import { TypeormsqliteService } from 'src/typeormsqlite/typeormsqlite.service';
import { MqttService } from 'src/mqtt/mqtt.service';
import { Inject } from '@nestjs/common';
import { PubSub } from 'graphql-subscriptions';
import { ModuleOT } from './ObjectTypes/moduleOT';
import { moduleAguaOT } from './ObjectTypes/moduleAguaOT';

@Resolver()
export class GraphQlserverResolver {
  constructor(
    private typeOrmService: TypeormsqliteService,
    private mqttservice: MqttService,
    @Inject('PUB_SUB') private pubSub: PubSub,
  ) {}

  @Query(() => [ModuleOT], { name: 'RetreiveAllModules' })
  async modules() {
    return this.typeOrmService.findAllModule();
  }

  @Query(() => [ModuleOT], { name: 'moduleAdded' })
  async LastModuleSavedStatic() {
    return this.typeOrmService.findLastModule();
  }

  @Query(() => [moduleAguaOT], { name: 'getAllModuleAgua' })
  async getallModuleAgua() {
    return this.typeOrmService.findAllModuleAgua();
  }

  @Query(() => [ModuleOT], { name: 'LastXModule' })
  async LastXModules(
    @Args('ammount', { type: () => Int }) ammount: number,
    @Args('Id', { type: () => Int }) Id: number,
  ) {
    return this.typeOrmService.findLastXModulo(ammount, Id);
  }

  @Query(() => moduleAguaOT, { name: 'FindLastAguaModule' })
  async lastAguaModule() {
    return this.typeOrmService.findLastModuleAgua();
  }

  @Mutation(() => Boolean, { name: 'changeValve' })
  async changeValve(
    @Args('moduleId', { type: () => Int }) moduleId: number,
    @Args('Value', { type: () => Boolean }) value: boolean,
  ) {
    const message = JSON.parse(JSON.stringify({ moduleId, value }));
    this.mqttservice.sendMqttMessage(`modulo/valve`, message);
    return value;
  }

  @Mutation(() => Boolean, { name: 'changePump' })
  async changePump(
    @Args('PumpState', { type: () => Boolean }) PumpState: boolean,
  ) {
    const message = JSON.parse(JSON.stringify({ PumpState }));
    this.mqttservice.sendMqttMessage(`pump/request`, message);
    return PumpState;
  }

  @Subscription(() => ModuleOT, { name: 'moduleAdded' })
  async moduleUpdate() {
    const sub = this.pubSub.asyncIterator('moduleAdded');
    return sub;
  }

  @Subscription(() => moduleAguaOT, { name: 'moduleAguaAdded' })
  async pumpUpdate() {
    return this.pubSub.asyncIterator('moduleAguaAdded');
  }

  @Query(() => [moduleAguaOT], { name: 'findModuleAguaBetweenInterval' })
  async findModuleAguaBetweenInterval(
    @Args('startDate') startDate: string,
    @Args('endDate') endDate: string,
  ): Promise<moduleAguaOT[]> {
    const date1 = new Date(startDate);
    const date2 = new Date(endDate);
    return this.typeOrmService.findModuleAguaBetweenInterval(date1, date2);
  }
}
