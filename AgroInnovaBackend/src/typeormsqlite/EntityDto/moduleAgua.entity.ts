import {
  Column,
  CreateDateColumn,
  Entity,
  PrimaryGeneratedColumn,
} from 'typeorm';

@Entity()
export class ModuleAguaEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  nivel: number;

  @Column()
  ph: number;

  @Column()
  pumpState: boolean;

  @CreateDateColumn({ type: 'datetime' })
  dateTime: Date;
}
