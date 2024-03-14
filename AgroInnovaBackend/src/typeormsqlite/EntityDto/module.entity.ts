/* eslint-disable @typescript-eslint/no-unused-vars */
import {
  Column,
  PrimaryGeneratedColumn,
  Entity,
  CreateDateColumn,
} from 'typeorm';

@Entity()
export class ModuleEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  moduleId: number;

  @Column()
  temperature: number;

  @Column()
  humidity: number;

  @Column()
  valve: boolean;

  @CreateDateColumn({ type: 'datetime' })
  dateTime: Date;

  @Column()
  client: number;
}
