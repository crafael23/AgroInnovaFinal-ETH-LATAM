import { Module } from '@nestjs/common';
import { GraphQlserverModule } from './graph-qlserver/graph-qlserver.module';
import { TypeormsqliteModule } from './typeormsqlite/typeormsqlite.module';

@Module({
  imports: [GraphQlserverModule, TypeormsqliteModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
