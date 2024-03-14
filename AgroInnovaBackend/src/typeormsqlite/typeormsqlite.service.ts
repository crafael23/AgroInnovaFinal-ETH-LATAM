/* eslint-disable @typescript-eslint/no-unused-vars */
import { Inject, Injectable, Module } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { ModuleEntity } from './EntityDto/module.entity';
import { ModuleDTO } from 'src/mqtt/MqttDTOs/ModuleDto';
import { PubSub } from 'graphql-subscriptions';
import { ModuleAguaEntity } from './EntityDto/moduleAgua.entity';
import { moduleAguaDTO } from 'src/mqtt/MqttDTOs/moduleAguaDTO';
import { HttpService } from '@nestjs/axios';

@Injectable()
export class TypeormsqliteService {
  constructor(
    @InjectRepository(ModuleEntity)
    private moduleRepository: Repository<ModuleEntity>,
    @InjectRepository(ModuleAguaEntity)
    private moduleAguaRepository: Repository<ModuleAguaEntity>,
    @Inject('PUB_SUB') private readonly pubSub: PubSub,
    private httpService: HttpService,
  ) {}

  async CreateModule(module: ModuleDTO): Promise<ModuleEntity> {
    const newModule: ModuleEntity = this.moduleRepository.create(module);
    const savedModule: ModuleEntity = await this.moduleRepository.save(
      newModule,
    );
    if (!savedModule) throw new Error('Error saving module');
    else {
      this.pubSub.publish('moduleAdded', { moduleAdded: savedModule });
      this.httpService
        .post(
          'http://bkyz2-fmaaa-aaaaa-qaaaq-cai.localhost:8000/sensorData',
          savedModule,
        )
        .subscribe(
          (response) => {
            console.log();
          },
          (error) => {
            console.log();
          },
        );
      return savedModule;
    }
  }

  async CreateModuleAgua(ModuleAgua: moduleAguaDTO): Promise<ModuleAguaEntity> {
    const newModuleAgua: ModuleAguaEntity =
      this.moduleAguaRepository.create(ModuleAgua);
    const savedModuleAgua: ModuleAguaEntity =
      await this.moduleAguaRepository.save(newModuleAgua);
    if (!savedModuleAgua) throw new Error('ErrorSaving Module');
    else {
      this.pubSub.publish('moduleAguaAdded', {
        moduleAguaAdded: savedModuleAgua,
      });
      return savedModuleAgua;
    }
  }

  async findAllModule(): Promise<ModuleEntity[]> {
    const query = this.moduleRepository
      .createQueryBuilder('Modules')
      .select([
        'id',
        'moduleId',
        'temperature',
        'humidity',
        'valve',
        'dateTime',
      ])
      .getRawMany<ModuleEntity>();
    return query;
  }

  async findAllModuleAgua(): Promise<ModuleAguaEntity[]> {
    const query = this.moduleAguaRepository.find();
    return query;
  }

  async findLastModuleAgua(): Promise<ModuleAguaEntity | null> {
    const query = await this.moduleAguaRepository
      .createQueryBuilder('moduleAgua')
      .orderBy('moduleAgua.id', 'DESC')
      .limit(1)
      .getOne();
    return query;
  }

  async findLastModule(): Promise<ModuleEntity[]> {
    const query = await this.moduleRepository
      .createQueryBuilder('modules')
      .select([
        'id',
        'moduleId',
        'temperature',
        'humidity',
        'valve',
        'MAX(dateTime) as dateTime',
      ])
      .groupBy('moduleId')
      .getRawMany<ModuleEntity>();

    for (const module of query) {
      module.dateTime = new Date(module.dateTime);
    }
    return query;
  }

  async findLastXModulo(
    ammount: number,
    id_provided: number,
  ): Promise<ModuleEntity[]> {
    return this.moduleRepository.find({
      where: { moduleId: id_provided },
      order: { id: 'DESC' },
      take: ammount,
    });
  }

  async findModuleAguaBetweenInterval(
    startDate: Date,
    endDate: Date,
  ): Promise<ModuleAguaEntity[]> {
    const query = await this.moduleAguaRepository
      .createQueryBuilder('data')
      .where('data.dateTime BETWEEN :startDate AND :endDate', {
        startDate,
        endDate,
      })
      .getMany();
    return query;
  }

  async findModuleBetweenInterval(
    moduleId: number,
    startDate: Date,
    endDate: Date,
  ): Promise<ModuleAguaEntity[]> {
    const query = await this.moduleAguaRepository
      .createQueryBuilder('data')
      .where('data.moduleId = :moduleId')
      .andWhere('data.dateTime BETWEEN :startDate AND :endDate', {
        moduleId,
        startDate,
        endDate,
      })
      .getMany();
    return query;
  }
}
