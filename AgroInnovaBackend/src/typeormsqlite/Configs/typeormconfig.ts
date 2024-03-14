import { TypeOrmModuleOptions } from '@nestjs/typeorm';
import { join } from 'path';

export const TypeOrmConfig: TypeOrmModuleOptions = {
  type: 'sqlite',
  database: 'database.sqlite',
  entities: [join(__dirname, '../**/**.entity{.ts,.js}')],
  extra: { timezone: 'CST' },
  synchronize: true,
};
